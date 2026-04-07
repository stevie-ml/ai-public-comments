"""
fetch_text.py
Re-fetch comment text from Regulations.gov by comment_id.

Usage:
    REGS_API_KEY=your_key python fetch_text.py [--input data/comments_v3.csv] [--output data/comments_with_text.csv]
"""

import os, sys, time, argparse
import pandas as pd
import requests
from pathlib import Path

BASE = 'https://api.regulations.gov/v4'
REGS_KEY = os.environ.get('REGS_API_KEY', '')


def fetch_text(comment_id, api_key):
    try:
        r = requests.get(
            f'{BASE}/comments/{comment_id}',
            headers={'X-Api-Key': api_key}, timeout=20,
        )
        if r.status_code == 429:
            time.sleep(60)
            return fetch_text(comment_id, api_key)
        attrs = r.json().get('data', {}).get('attributes', {})
        return (attrs.get('comment', '') or '').strip()
    except Exception as e:
        print(f'  Error fetching {comment_id}: {e}')
        return ''


if __name__ == '__main__':
    if not REGS_KEY:
        sys.exit('ERROR: set REGS_API_KEY')

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='data/comments_v3.csv')
    parser.add_argument('--output', default='data/comments_with_text.csv')
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    df = pd.read_csv(root / args.input)

    # Resume if output exists
    done_ids = set()
    if (root / args.output).exists():
        done = pd.read_csv(root / args.output)
        done_ids = set(done['comment_id'])
        print(f'Resuming: {len(done_ids)} already fetched')

    results = []
    remaining = df[~df['comment_id'].isin(done_ids)]
    print(f'Fetching text for {len(remaining)} comments...')

    for i, row in enumerate(remaining.itertuples(index=False)):
        cid = row.comment_id
        print(f'[{i+1}/{len(remaining)}] {cid}', end=' ', flush=True)
        text = fetch_text(cid, REGS_KEY)
        wc = len(text.split()) if text else 0
        print(f'({wc}w)')
        results.append({'comment_id': cid, 'text': text})
        time.sleep(0.7)

        if len(results) % 100 == 0:
            chunk = pd.DataFrame(results)
            if (root / args.output).exists():
                existing = pd.read_csv(root / args.output)
                chunk = pd.concat([existing, chunk]).drop_duplicates(subset='comment_id')
            chunk.to_csv(root / args.output, index=False)
            results = []
            print(f'  [checkpoint: {len(chunk)} saved]')

    if results:
        chunk = pd.DataFrame(results)
        if (root / args.output).exists():
            existing = pd.read_csv(root / args.output)
            chunk = pd.concat([existing, chunk]).drop_duplicates(subset='comment_id')
        chunk.to_csv(root / args.output, index=False)

    print(f'Done -> {args.output}')
