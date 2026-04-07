"""
02_score_llm.py
Classify public comments using Claude Haiku for regulatory stance,
ideology signal, argument type, and argument quality.

Samples AI-flagged comments (score=1.0) and a stratified human sample
(score=0.0), fetches text from Regulations.gov, and scores with Haiku.

Output: data/comments_v3_llm.csv

Usage:
    ANTHROPIC_API_KEY=sk-... REGS_API_KEY=your_key python 02_score_llm.py
"""

import os, sys, time, json
import pandas as pd
import requests
import anthropic
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

REGS_KEY      = os.environ.get('REGS_API_KEY', '')
ANTHROPIC_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
if not REGS_KEY or not ANTHROPIC_KEY:
    sys.exit('ERROR: set REGS_API_KEY and ANTHROPIC_API_KEY')

BASE          = 'https://api.regulations.gov/v4'
HUMAN_SAMPLE  = 275
DATA_IN       = Path(__file__).resolve().parent.parent / 'data' / 'comments_v3.csv'
OUT           = Path(__file__).resolve().parent.parent / 'data' / 'comments_v3_llm.csv'

claude = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

SCORE_PROMPT = """\
You are a political scientist coding public comments submitted to U.S. federal agencies.

Read the comment below and return a JSON object with exactly these fields:

{
  "regulatory_stance": "anti_regulation" | "pro_regulation" | "neutral" | "unclear",
  "ideology_signal":   "right" | "left" | "centrist" | "unclear",
  "argument_type":     "technical" | "emotional" | "form_letter" | "substantive_novel",
  "argument_quality":  1-5,
  "key_claim":         "one sentence summarizing the core argument"
}

Definitions:
- regulatory_stance: does the commenter oppose (anti) or support (pro) the proposed rule?
  "neutral" = asks questions or provides data without taking a side.
- ideology_signal: is the framing consistent with right-leaning (market, liberty, burden)
  or left-leaning (equity, protection, corporate power) political discourse?
  Score the rhetoric, not your assumption about what side benefits.
- argument_type:
    technical = cites data, law, or specific regulatory text
    emotional = personal story or moral appeal without factual basis
    form_letter = generic boilerplate that could apply to any rule
    substantive_novel = raises a specific factual or legal point not obvious from the rule
- argument_quality: 1 = pure noise, 5 = would require an agency response under APA

Return ONLY the JSON. No explanation.

COMMENT:
"""


def fetch_comment_text(comment_id):
    """Fetch inline text for a single comment from Regulations.gov."""
    try:
        r = requests.get(
            f'{BASE}/comments/{comment_id}',
            headers={'X-Api-Key': REGS_KEY}, timeout=20,
        )
        time.sleep(0.7)
        attrs = r.json().get('data', {}).get('attributes', {})
        return (attrs.get('comment', '') or '').strip()
    except Exception:
        return ''


def score_with_haiku(text, comment_id):
    """Score a single comment. Returns dict or None."""
    try:
        msg = claude.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=200,
            messages=[{'role': 'user', 'content': SCORE_PROMPT + text[:4000]}],
        )
        raw = msg.content[0].text.strip()
        if raw.startswith('```'):
            raw = raw.split('```')[1]
            if raw.startswith('json'):
                raw = raw[4:]
        return json.loads(raw)
    except Exception as e:
        print(f'  Haiku error on {comment_id}: {e}')
        return None


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    df = pd.read_csv(DATA_IN)
    df = df[df['ai_score'].notna()]

    ai_comments = df[df['ai_score'] == 1.0].copy()
    human_comments = df[df['ai_score'] == 0.0].copy()

    # Stratified human sample matching AI category distribution
    ai_cat_counts = ai_comments['category'].value_counts(normalize=True)
    human_parts = []
    for cat, frac in ai_cat_counts.items():
        n = max(1, round(frac * HUMAN_SAMPLE))
        pool = human_comments[human_comments['category'] == cat]
        human_parts.append(pool.sample(min(n, len(pool)), random_state=42))
    human_sample = pd.concat(human_parts).drop_duplicates(subset='comment_id')

    print(f'AI: {len(ai_comments)} | Human sample: {len(human_sample)}')

    to_score = pd.concat([ai_comments, human_sample])[
        ['comment_id', 'docket_id', 'agency', 'category', 'year', 'posted_date', 'ai_score']
    ].copy()

    # Resume
    done = pd.DataFrame()
    if OUT.exists():
        done = pd.read_csv(OUT)
        to_score = to_score[~to_score['comment_id'].isin(set(done['comment_id']))]
        print(f'Resuming: {len(done)} done, {len(to_score)} remaining')

    rows = []
    for i, row in enumerate(to_score.itertuples(index=False)):
        cid = row.comment_id
        print(f'[{i+1}/{len(to_score)}] {cid}', end=' ', flush=True)

        text = fetch_comment_text(cid)
        if not text or len(text.split()) < 10:
            print('(no text)')
            continue

        time.sleep(0.3)
        scores = score_with_haiku(text, cid)
        if scores is None:
            print('(failed)')
            continue

        rows.append({
            'comment_id': cid, 'docket_id': row.docket_id,
            'agency': row.agency, 'category': row.category,
            'year': row.year, 'posted_date': row.posted_date,
            'ai_score': row.ai_score, 'word_count': len(text.split()),
            'regulatory_stance': scores.get('regulatory_stance', 'unclear'),
            'ideology_signal': scores.get('ideology_signal', 'unclear'),
            'argument_type': scores.get('argument_type', 'unclear'),
            'argument_quality': scores.get('argument_quality', 0),
            'key_claim': scores.get('key_claim', ''),
        })
        print(f"-> {scores.get('regulatory_stance','?')} / {scores.get('ideology_signal','?')}")

        if len(rows) % 50 == 0:
            chunk = pd.DataFrame(rows)
            done = pd.concat([done, chunk]).drop_duplicates(subset='comment_id', keep='last')
            done.to_csv(OUT, index=False)
            rows = []
            print(f'  [checkpoint: {len(done)} total]')

    if rows:
        chunk = pd.DataFrame(rows)
        done = pd.concat([done, chunk]).drop_duplicates(subset='comment_id', keep='last')
        done.to_csv(OUT, index=False)

    print(f'\nDone. {len(done)} comments scored -> {OUT}')
