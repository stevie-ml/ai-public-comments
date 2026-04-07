"""
04_ideology_analysis.py
Ideological alignment analysis for Section 4.7 of the paper.

Tests whether AI-generated comments differ from human comments in
regulatory stance, ideological framing, and argument quality.

Output: prints tables and statistics; saves fig4_ideology.png

Usage:
    python 04_ideology_analysis.py
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, mannwhitneyu, fisher_exact
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / 'data' / 'comments_v3_llm.csv'
OUT  = Path(__file__).resolve().parent.parent / 'paper' / 'figures'

df = pd.read_csv(DATA)
df['is_ai'] = (df['ai_score'] == 1.0).astype(int)
df['is_human'] = (df['ai_score'] == 0.0).astype(int)

print(f"N = {len(df)} classified comments")
print(f"  AI (score=1.0): {df['is_ai'].sum()}")
print(f"  Human (score=0.0): {df['is_human'].sum()}")

# ── 1. Regulatory Stance x AI ────────────────────────────────────────────────

print("\n" + "=" * 60)
print("REGULATORY STANCE x AI STATUS")
print("=" * 60)

for label, mask in [('AI', df['is_ai'] == 1), ('Human', df['is_human'] == 1)]:
    sub = df[mask]
    print(f"\n{label} (n={len(sub)}):")
    for stance in ['pro_regulation', 'anti_regulation', 'neutral', 'unclear']:
        n = (sub['regulatory_stance'] == stance).sum()
        print(f"  {stance:20s}: {n:4d} ({n/len(sub)*100:5.1f}%)")

# Chi-squared: pro/anti only
clean = df[
    df['regulatory_stance'].isin(['pro_regulation', 'anti_regulation']) &
    (df['is_ai'] + df['is_human'] == 1)
]
ct = pd.crosstab(clean['regulatory_stance'], clean['is_ai'])
chi2, p, dof, _ = chi2_contingency(ct)
print(f"\nChi-squared (pro/anti x AI): chi2={chi2:.3f}, p={p:.4f}")

# ── 2. Ideology x AI ─────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("IDEOLOGY SIGNAL x AI STATUS")
print("=" * 60)

for label, mask in [('AI', df['is_ai'] == 1), ('Human', df['is_human'] == 1)]:
    sub = df[mask]
    print(f"\n{label} (n={len(sub)}):")
    for ideo in ['left', 'right', 'centrist', 'unclear']:
        n = (sub['ideology_signal'] == ideo).sum()
        print(f"  {ideo:20s}: {n:4d} ({n/len(sub)*100:5.1f}%)")

clean2 = df[
    df['ideology_signal'].isin(['left', 'right']) &
    (df['is_ai'] + df['is_human'] == 1)
]
ct2 = pd.crosstab(clean2['ideology_signal'], clean2['is_ai'])
chi2_2, p2, dof2, _ = chi2_contingency(ct2)
print(f"\nChi-squared (left/right x AI): chi2={chi2_2:.3f}, p={p2:.4f}")

# Fisher's exact for robustness
or_val, p_fisher = fisher_exact(ct2.values)
print(f"Fisher's exact: OR={or_val:.3f}, p={p_fisher:.4f}")

# ── 3. Agency-level stance comparison ─────────────────────────────────────────

print("\n" + "=" * 60)
print("STANCE BY AGENCY")
print("=" * 60)

for agency in df['agency'].value_counts().index:
    asub = df[df['agency'] == agency]
    ai_sub = asub[asub['is_ai'] == 1]
    hu_sub = asub[asub['is_human'] == 1]
    if len(ai_sub) < 3:
        continue
    ai_pro = (ai_sub['regulatory_stance'] == 'pro_regulation').mean() * 100
    hu_pro = (hu_sub['regulatory_stance'] == 'pro_regulation').mean() * 100
    ai_anti = (ai_sub['regulatory_stance'] == 'anti_regulation').mean() * 100
    hu_anti = (hu_sub['regulatory_stance'] == 'anti_regulation').mean() * 100
    diff = ai_pro - hu_pro
    print(f"{agency:6s} (AI={len(ai_sub):2d}, H={len(hu_sub):2d}): "
          f"AI pro={ai_pro:5.1f}% anti={ai_anti:5.1f}% | "
          f"Human pro={hu_pro:5.1f}% anti={hu_anti:5.1f}% | "
          f"diff={diff:+.1f}pp")

# ── 4. Argument quality ───────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("ARGUMENT QUALITY")
print("=" * 60)

ai_q = df[df['is_ai'] == 1]['argument_quality']
hu_q = df[df['is_human'] == 1]['argument_quality']
u, p_mw = mannwhitneyu(ai_q, hu_q, alternative='two-sided')
print(f"AI: mean={ai_q.mean():.2f}, median={ai_q.median():.1f}")
print(f"Human: mean={hu_q.mean():.2f}, median={hu_q.median():.1f}")
print(f"Mann-Whitney U={u:.0f}, p={p_mw:.4f}")

print("\nArgument type distribution:")
ct3 = pd.crosstab(df['argument_type'], df['is_ai'].map({1: 'AI', 0: 'Human'}),
                   normalize='columns').round(3)
print(ct3)

# ── 5. Key interaction: stance x ideology x AI ───────────────────────────────

print("\n" + "=" * 60)
print("STANCE x IDEOLOGY x AI (key cross-tab)")
print("=" * 60)

for label, mask in [('AI', df['is_ai'] == 1), ('Human', df['is_human'] == 1)]:
    sub = df[mask]
    print(f"\n{label} (n={len(sub)}):")
    print(pd.crosstab(sub['regulatory_stance'], sub['ideology_signal']))

# ── 6. Amplification pattern ─────────────────────────────────────────────────

print("\n" + "=" * 60)
print("AMPLIFICATION PATTERN: does AI amplify the majority position?")
print("=" * 60)

amplifies = 0
total_agencies = 0
for agency in df['agency'].value_counts().index:
    asub = df[df['agency'] == agency]
    ai_sub = asub[asub['is_ai'] == 1]
    hu_sub = asub[asub['is_human'] == 1]
    if len(ai_sub) < 3 or len(hu_sub) < 3:
        continue
    total_agencies += 1
    hu_pro = (hu_sub['regulatory_stance'] == 'pro_regulation').mean()
    ai_pro = (ai_sub['regulatory_stance'] == 'pro_regulation').mean()
    hu_majority_is_pro = hu_pro > 0.5
    ai_more_pro = ai_pro > hu_pro
    if hu_majority_is_pro == ai_more_pro:
        amplifies += 1
        direction = "amplifies"
    else:
        direction = "REVERSES"
    print(f"  {agency:6s}: human majority={'pro' if hu_majority_is_pro else 'anti':4s}, "
          f"AI shift={'more pro' if ai_more_pro else 'more anti':9s} -> {direction}")

print(f"\nAI amplifies majority position in {amplifies}/{total_agencies} agencies "
      f"({amplifies/total_agencies*100:.0f}%)")
