"""
05_pangram_validation.py
Validate Pangram AI detection by comparing:
  1. Real 2018 public comments (pre-ChatGPT, definitively human)
  2. AI-generated comments matched to the same topics/agencies

Fetches 20 real comments from 2018, generates 20 matched AI comments,
scores all 40 with Pangram, and reports accuracy.

Usage:
    REGS_API_KEY=your_key PANGRAM_API_KEY=your_key python 05_pangram_validation.py
"""

import os, sys, time, json, random
import requests
import pandas as pd
from pathlib import Path

REGS_KEY = os.environ.get('REGS_API_KEY', '')
PANG_KEY = os.environ.get('PANGRAM_API_KEY', '')
if not REGS_KEY or not PANG_KEY:
    sys.exit('Set REGS_API_KEY and PANGRAM_API_KEY')

BASE     = 'https://api.regulations.gov/v4'
PANG_URL = 'https://text.api.pangram.com/v3'
OUT      = Path(__file__).resolve().parent.parent / 'data' / 'pangram_validation.csv'

# Agencies to sample from
AGENCIES = ['IRS', 'EPA', 'OSHA', 'NPS', 'USCIS', 'CMS', 'BLM', 'NHTSA', 'DOE', 'USDA']


def regs_get(path, params):
    for attempt in range(3):
        try:
            r = requests.get(f'{BASE}/{path}', headers={'X-Api-Key': REGS_KEY},
                             params=params, timeout=20)
            time.sleep(0.8)
            if r.status_code == 429:
                time.sleep(60)
                continue
            return r.json() if r.status_code == 200 else {}
        except:
            time.sleep(5)
    return {}


def fetch_2018_comments(n=20):
    """Fetch n real comments from 2018."""
    comments = []
    random.shuffle(AGENCIES)
    per_agency = max(2, n // len(AGENCIES))

    for agency in AGENCIES:
        if len(comments) >= n:
            break
        print(f'  Fetching from {agency} 2018...', end=' ', flush=True)
        d = regs_get('comments', {
            'filter[agencyId]': agency,
            'filter[postedDate][ge]': '2018-01-01',
            'filter[postedDate][le]': '2018-12-31',
            'page[size]': 25,
        })
        total = d.get('meta', {}).get('totalElements', 0) or 0
        if total < 5:
            print(f'only {total}')
            continue

        stubs = d.get('data', [])
        random.shuffle(stubs)
        found = 0

        for stub in stubs[:per_agency * 3]:
            if len(comments) >= n:
                break
            cid = stub.get('id', '')
            detail = regs_get(f'comments/{cid}', {})
            attrs = detail.get('data', {}).get('attributes', {})
            text = (attrs.get('comment', '') or '').strip()
            wc = len(text.split())
            if wc < 50 or wc > 800:
                continue
            comments.append({
                'comment_id': cid,
                'agency': agency,
                'text': text,
                'word_count': wc,
                'source': 'human_2018',
                'topic': attrs.get('title', '') or attrs.get('docketId', ''),
            })
            found += 1
        print(f'{found} found')

    return comments[:n]


def pangram_score(text):
    chunk = ' '.join(text.split()[:5000])
    for attempt in range(3):
        try:
            r = requests.post(PANG_URL,
                              headers={'x-api-key': PANG_KEY, 'Content-Type': 'application/json'},
                              json={'text': chunk}, timeout=60)
            if r.status_code == 402:
                print('PANGRAM CREDITS EXHAUSTED')
                return None, None
            if r.status_code == 429:
                time.sleep(30)
                continue
            r.raise_for_status()
            d = r.json()
            return d.get('fraction_ai'), d.get('fraction_human')
        except:
            time.sleep(5)
    return None, None


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("Step 1: Fetching real 2018 comments...")
    humans = fetch_2018_comments(20)
    print(f"Got {len(humans)} human comments\n")

    # Save human comments for reference
    for h in humans:
        print(f"  [{h['agency']}] {h['word_count']}w: {h['text'][:80]}...")

    print(f"\nStep 2: AI comments should be generated separately and added to this script.")
    print("Step 3: Scoring with Pangram...")

    all_comments = humans  # AI comments will be appended

    results = []
    for i, c in enumerate(all_comments):
        print(f"[{i+1}/{len(all_comments)}] {c['source']:12s} {c['agency']:6s} {c['word_count']}w",
              end=' ', flush=True)
        ai_score, human_score = pangram_score(c['text'])
        if ai_score is None:
            print('FAILED')
            continue
        print(f"ai={ai_score:.3f}")
        results.append({**c, 'ai_score': ai_score, 'human_score': human_score})
        time.sleep(0.5)

    df = pd.DataFrame(results)
    df.to_csv(OUT, index=False)

    # Report
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    for source in df['source'].unique():
        sub = df[df['source'] == source]
        print(f"\n{source} (n={len(sub)}):")
        print(f"  Mean AI score:  {sub['ai_score'].mean():.3f}")
        print(f"  Median:         {sub['ai_score'].median():.3f}")
        print(f"  % flagged >0.5: {(sub['ai_score'] > 0.5).mean()*100:.1f}%")
        print(f"  Min/Max:        {sub['ai_score'].min():.3f} / {sub['ai_score'].max():.3f}")

    if df['source'].nunique() == 2:
        human_correct = (df[df['source'] == 'human_2018']['ai_score'] < 0.5).mean()
        ai_correct = (df[df['source'] == 'ai_generated']['ai_score'] > 0.5).mean()
        accuracy = (human_correct + ai_correct) / 2
        print(f"\nAccuracy:")
        print(f"  Human correctly identified: {human_correct*100:.1f}%")
        print(f"  AI correctly identified:    {ai_correct*100:.1f}%")
        print(f"  Balanced accuracy:          {accuracy*100:.1f}%")
