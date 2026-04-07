"""
01_collect_v3.py
Collect public comments from Regulations.gov and score with Pangram AI detection.

Full cabinet-department sample with improved randomness:
  1. Full-range page sampling across Regulations.gov
  2. Docket stratification (round-robin across dockets within each agency-year)

Target: 65 scored comments per agency x year cell
        18 agencies x 7 years (2019-2025)

Output: data/comments_v3.csv

Requires:
  - Regulations.gov API key (free: https://open.gsa.gov/api/regulationsgov/)
  - Pangram API key (https://pangram.com)

Usage:
    REGS_API_KEY=your_key PANGRAM_API_KEY=your_key python 01_collect_v3.py
"""

import os, sys, requests, time, re, random, io
import pandas as pd
import pdfplumber
from pathlib import Path
from collections import defaultdict

# ── Config ────────────────────────────────────────────────────────────────────

REGS_KEY   = os.environ.get('REGS_API_KEY', '')
PANG_KEY   = os.environ.get('PANGRAM_API_KEY', '')
if not REGS_KEY or not PANG_KEY:
    sys.exit('ERROR: set REGS_API_KEY and PANGRAM_API_KEY environment variables')

BASE       = 'https://api.regulations.gov/v4'
PANG_URL   = 'https://text.api.pangram.com/v3'
OUT        = Path(__file__).resolve().parent.parent / 'data' / 'comments_v3.csv'

YEARS      = list(range(2019, 2026))
PER_CELL   = 65
MIN_WORDS  = 50
WORD_CAP   = 5000
REGS_SLEEP = 0.7
MAX_PAGES  = 40
API_PAGE_CAP = 40

AGENCIES = {
    'IRS': 'finance', 'OCC': 'finance',
    'NPS': 'public_lands', 'BLM': 'public_lands',
    'FWS': 'environment', 'BOEM': 'energy',
    'USDA': 'agriculture',
    'CMS': 'health',
    'NOAA': 'environment',
    'OSHA': 'labor',
    'NHTSA': 'transportation',
    'DOE': 'energy',
    'ED': 'education',
    'VA': 'veterans',
    'USCIS': 'immigration', 'EOIR': 'immigration',
    'EPA': 'environment',
}

FALLBACK_DOCKETS = {
    'EPA': [
        'EPA-HQ-OAR-2017-0355', 'EPA-HQ-OW-2018-0149',
        'EPA-HQ-OAR-2021-0317', 'EPA-HQ-OAR-2023-0072',
    ],
    'BLM': [
        'BLM-2022-0014', 'BLM-2023-0007', 'BLM-2025-0001',
    ],
    'FWS': [
        'FWS-HQ-ES-2018-0097', 'FWS-HQ-ES-2024-0001',
    ],
    'EOIR': [
        'EOIR-2020-0003', 'EOIR-2024-0001',
    ],
    'ED': [
        'ED-2021-OCR-0166', 'ED-2022-OCR-0143',
    ],
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def clean(raw):
    t = re.sub(r'<[^>]+>', ' ', raw or '')
    t = re.sub(r'&[a-z#0-9]+;', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def extract_pdf_text(url):
    """Download PDF attachment and extract text (max 20 pages)."""
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200 or 'pdf' not in r.headers.get('content-type', '').lower():
            return ''
        with pdfplumber.open(io.BytesIO(r.content)) as pdf:
            pages = [p.extract_text() or '' for p in pdf.pages[:20]]
        return re.sub(r'\s+', ' ', ' '.join(pages)).strip()
    except Exception:
        return ''


def regs_get(path, params, retries=4):
    for attempt in range(retries):
        try:
            r = requests.get(
                f'{BASE}/{path}',
                headers={'X-Api-Key': REGS_KEY},
                params=params, timeout=30,
            )
            time.sleep(REGS_SLEEP)
            if r.status_code == 429:
                print('  [429 rate limit, sleeping 60s]')
                time.sleep(60)
                continue
            if r.text.strip():
                return r.json()
        except requests.exceptions.Timeout:
            time.sleep(15 * (attempt + 1))
        except Exception as e:
            print(f'  [err: {e}]')
            time.sleep(8)
    return {}


def pangram_score(text):
    chunk = ' '.join(text.split()[:WORD_CAP])
    for attempt in range(4):
        try:
            r = requests.post(
                PANG_URL,
                headers={'x-api-key': PANG_KEY, 'Content-Type': 'application/json'},
                json={'text': chunk}, timeout=90,
            )
            if r.status_code == 402:
                return 'EXHAUSTED'
            if r.status_code == 429:
                time.sleep(30)
                continue
            r.raise_for_status()
            d = r.json()
            return (d.get('fraction_ai'), d.get('fraction_human'),
                    d.get('fraction_ai_assisted', 0.0))
        except requests.exceptions.Timeout:
            time.sleep(15 * (attempt + 1))
        except Exception as e:
            print(f'err:{e} ', end='')
            time.sleep(10)
    return None


def checkpoint(new_rows):
    if not new_rows:
        return
    new_df = pd.DataFrame(new_rows)
    if OUT.exists():
        existing = pd.read_csv(OUT)
        combined = pd.concat([existing, new_df], ignore_index=True)
    else:
        combined = new_df
    combined = combined.drop_duplicates(subset='comment_id', keep='first')
    combined.to_csv(OUT, index=False)
    return len(combined)


def collect_cell(agency, year, need, seen_ids, seen_fps):
    """Collect comments for one agency-year cell using random page sampling."""
    date_ge = f'{year}-01-01'
    date_le = f'{year}-12-31'

    probe = regs_get('comments', {
        'filter[agencyId]': agency,
        'filter[postedDate][ge]': date_ge,
        'filter[postedDate][le]': date_le,
        'page[size]': 5,
    })
    total = probe.get('meta', {}).get('totalElements', 0) or 0
    if total < 5:
        return []

    max_page = max(1, min(total // 25, API_PAGE_CAP))
    pages = random.sample(range(1, max_page + 1), min(MAX_PAGES, max_page))

    # Collect stubs across random pages
    all_stubs = []
    for page in pages:
        d = regs_get('comments', {
            'filter[agencyId]': agency,
            'filter[postedDate][ge]': date_ge,
            'filter[postedDate][le]': date_le,
            'page[size]': 25, 'page[number]': page,
        })
        all_stubs.extend(d.get('data', []))

    # Docket stratification: round-robin across dockets
    by_docket = defaultdict(list)
    for stub in all_stubs:
        did = stub.get('attributes', {}).get('docketId') or 'unknown'
        by_docket[did].append(stub)

    docket_lists = list(by_docket.values())
    random.shuffle(docket_lists)
    balanced = []
    while len(balanced) < need * 4 and any(docket_lists):
        for dl in docket_lists:
            if dl and len(balanced) < need * 4:
                balanced.append(dl.pop(random.randrange(len(dl))))

    collected = []

    def try_stubs(stubs_list):
        empty_streak = 0
        for stub in stubs_list:
            if len(collected) >= need:
                break
            if empty_streak >= 100:
                break
            cid = stub.get('id', '')
            if not cid or cid in seen_ids:
                continue
            detail = regs_get(f'comments/{cid}', {'include': 'attachments'})
            attrs = detail.get('data', {}).get('attributes', {})
            text = clean(attrs.get('comment', ''))
            if len(text.split()) < MIN_WORDS:
                attachments = detail.get('included') or []
                for att in attachments:
                    for fmt in att.get('attributes', {}).get('fileFormats', []):
                        if 'pdf' in fmt.get('format', '').lower():
                            pdf_text = extract_pdf_text(fmt['fileUrl'])
                            if len(pdf_text.split()) >= MIN_WORDS:
                                text = pdf_text
                            break
                    if len(text.split()) >= MIN_WORDS:
                        break
            wc = len(text.split())
            if wc < MIN_WORDS:
                empty_streak += 1
                continue
            empty_streak = 0
            fp = ' '.join(text.split()[:15])
            if fp in seen_fps:
                continue
            posted = (attrs.get('postedDate') or '')[:10]
            posted_year = int(posted[:4]) if len(posted) >= 4 else year
            seen_ids.add(cid)
            seen_fps.add(fp)
            collected.append({
                'comment_id': cid, 'docket_id': attrs.get('docketId', ''),
                'posted_date': posted, 'year': posted_year,
                'word_count': wc, 'text': text,
            })
            print(f'    [{len(collected)}/{need}] {cid} ({wc}w)')

    try_stubs(balanced)

    if len(collected) < need and agency in FALLBACK_DOCKETS:
        for did in FALLBACK_DOCKETS[agency]:
            if len(collected) >= need:
                break
            d = regs_get('comments', {
                'filter[docketId]': did,
                'filter[postedDate][ge]': date_ge,
                'filter[postedDate][le]': date_le,
                'page[size]': 5,
            })
            total_d = d.get('meta', {}).get('totalElements', 0) or 0
            if total_d < 3:
                continue
            max_pg_d = max(1, total_d // 25)
            pages_d = random.sample(range(1, max_pg_d + 1), min(30, max_pg_d))
            fb_stubs = []
            for pg in pages_d:
                r = regs_get('comments', {
                    'filter[docketId]': did,
                    'filter[postedDate][ge]': date_ge,
                    'filter[postedDate][le]': date_le,
                    'page[size]': 25, 'page[number]': pg,
                })
                fb_stubs.extend(r.get('data', []))
            random.shuffle(fb_stubs)
            try_stubs(fb_stubs)

    return collected


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    random.seed()
    seen_ids, seen_fps, have = set(), set(), defaultdict(int)

    if OUT.exists():
        existing = pd.read_csv(OUT)
        print(f'Resuming: {len(existing)} rows')
        for _, row in existing[existing['ai_score'].notna()].iterrows():
            ag = str(row.get('agency', '') or '')
            try:
                yr = int(row['year'])
            except (ValueError, TypeError):
                continue
            if str(row.get('comment_id', '')):
                seen_ids.add(str(row['comment_id']))
            have[(ag, yr)] += 1

    pending = []
    for agency, category in AGENCIES.items():
        print(f'\n[{agency}]')
        for year in YEARS:
            need = max(0, PER_CELL - have.get((agency, year), 0))
            if need == 0:
                continue
            print(f'  {year}: need {need}')
            raw = collect_cell(agency, year, need, seen_ids, seen_fps)
            for c in raw:
                result = pangram_score(c['text'])
                if result == 'EXHAUSTED':
                    print('Pangram credits exhausted.')
                    checkpoint(pending)
                    sys.exit(0)
                if result is None or result[0] is None:
                    continue
                ai, human, assisted = result
                pending.append({
                    'comment_id': c['comment_id'], 'docket_id': c['docket_id'],
                    'agency': agency, 'category': category,
                    'year': c['year'], 'posted_date': c['posted_date'],
                    'word_count': c['word_count'],
                    'ai_score': round(ai, 4), 'ai_assisted': round(assisted, 4),
                    'human_score': round(human, 4),
                })
                if len(pending) >= 50:
                    total = checkpoint(pending)
                    print(f'  [checkpoint: {total} rows]')
                    pending = []

    if pending:
        checkpoint(pending)
    print('Done.')
