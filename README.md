# Who Uses AI to Comment on Federal Rules?

Replication package for "Who Uses AI to Comment on Federal Rules?" by Stevie Miller.

## Summary

This paper provides the first systematic measurement of AI-generated content in federal public comments submitted through Regulations.gov. Using the Pangram AI detection API, I score 5,326 comments across 18 agencies and 7 years (2019--2025). I find that 18.3% of 2025 comments show detectable AI content, with adoption driven by adversarial political mobilization rather than technological diffusion. AI-generated comments are disproportionately left-leaning in rhetorical framing and amplify the dominant position within each regulatory docket.

## Data

| File | Rows | Description |
|------|------|-------------|
| `data/comments_v3.csv` | 5,326 | Full scored dataset: 18 agencies, 2019--2025, Pangram AI scores |
| `data/comments_v3_llm.csv` | 414 | LLM-classified subset: regulatory stance, ideology, argument type |
| `data/comments_merged.csv` | 498 | Cross-sectional sample used in main paper tables (16 agencies, 2025) |
| `data/comments_timeseries.csv` | 2,885 | Longitudinal panel for time-series analysis |
| `data/docket_impact.csv` | 62 | Final rule presence and comment influence scores per docket |

Comment text is not included in the repository due to size. Text can be re-fetched from Regulations.gov using the `comment_id` column and the script `scripts/fetch_text.py`.

## Scripts

Scripts are numbered in order of execution:

| Script | Purpose |
|--------|---------|
| `scripts/01_collect_v3.py` | Collect comments from Regulations.gov API and score with Pangram |
| `scripts/02_score_llm.py` | Classify comments (stance, ideology, argument type) using Claude Haiku |
| `scripts/03_analysis.R` | Main figures and regression tables |
| `scripts/04_ideology_analysis.py` | Ideological alignment analysis (Section 4.7) |
| `scripts/fetch_text.py` | Re-fetch comment text from Regulations.gov by comment_id |

## Requirements

**Python 3.10+**
```
pip install pandas requests anthropic scipy
```

**R 4.0+**
```r
install.packages(c("tidyverse", "lmtest", "sandwich", "stargazer", "lubridate"))
```

## API Keys Required

- **Regulations.gov**: Free key at https://open.gsa.gov/api/regulationsgov/
- **Pangram AI Detection**: https://pangram.com (for re-running AI scoring)
- **Anthropic**: https://console.anthropic.com (for re-running LLM classification)

## Figures

- `paper/figures/fig1_agency_ai.png` -- AI adoption by agency (main figure)
- `paper/figures/fig2_wordcount.png` -- Word count by AI score group
- `paper/figures/fig3_timeseries.png` -- Time series of AI adoption 2019--2025
- `paper/figures/fig3b_scatter.png` -- Individual comment scores by agency and year
- `paper/figures/fig4_ideology.png` -- Ideological alignment of AI vs human comments

## License

Data sourced from Regulations.gov (public domain). Code: MIT License.

## Citation

```
Miller, S. (2026). Who Uses AI to Comment on Federal Rules? Working Paper.
```
