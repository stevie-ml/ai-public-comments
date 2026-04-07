# Who Uses AI to Comment on Federal Rules?

**Stevie Miller**
Carnegie Mellon University
March 2026

---

## Abstract

I use AI detection scores from Pangram to measure the prevalence of AI-generated content in 498 public comments submitted to sixteen federal agencies in 2025. I find that 18.3% of comments show detectable AI content, but adoption is highly uneven across regulatory context. Comments on politically adversarial rules — Bureau of Land Management public lands rescissions and USCIS alien registration requirements — show AI adoption rates of 30.9% and 23.6%, respectively. Health policy comments on HRSA's 340B drug pricing rule show the highest adoption rate at 40%, suggesting AI use extends beyond grassroots political mobilization to organized industry stakeholder campaigns. Comments on routine technical rules (USDA, DOL) show near-zero adoption. AI-generated comments are meaningfully longer than human-written comments. These patterns suggest AI adoption in public comments is driven by adversarial mobilization rather than technological diffusion, with implications for the integrity of the notice-and-comment process.

---

## 1. Introduction

The notice-and-comment process is the primary mechanism through which American citizens participate in federal rulemaking. Under the Administrative Procedure Act, agencies must publish proposed rules and accept public comment before finalizing them. Courts have struck down rules when agencies failed to meaningfully consider public input. The assumption underlying this system is that comments represent authentic expressions of public preference.

The emergence of large language models has challenged this assumption. Since ChatGPT's release in November 2022, generating polished, structured prose has become trivially easy. A citizen who previously submitted "please don't do this, it's bad for my community" can now prompt an AI to produce a 250-word argument citing policy history, constitutional concerns, and economic impacts. An advocacy organization that once spent staff time drafting a single form letter can now generate thousands of individually-varied versions.

This paper provides the first systematic measurement of AI adoption in federal public comments. I collect 498 public comments from sixteen federal agencies in 2025 and score each with the Pangram AI detection API, which returns a continuous measure of the probability that a given text was AI-generated. I also construct a longitudinal panel of 490 scored comments spanning 2019–2025 across six agencies to test whether AI adoption follows the post-ChatGPT inflection point documented in other domains. My analysis addresses three questions: (1) How prevalent is AI use in public comments? (2) Which regulatory contexts attract the most AI use? (3) Has AI adoption grown since ChatGPT's release, and does that growth vary by regulatory context?

My central finding is that AI adoption is highly uneven and driven by political context rather than technological availability. Agencies receiving comments on politically charged rules — BLM's rescission of public lands conservation rules, USCIS's new alien registration requirements — show AI adoption rates near 30%, with many individual comments scoring at the maximum (1.0). Health policy dockets (HRSA's 340B drug pricing rule) show the highest adoption rate at 40%, suggesting organized industry stakeholder campaigns alongside grassroots mobilization. Agencies receiving comments on routine administrative matters (USDA agriculture rules, DOL labor notices) show near-zero adoption. This pattern holds within the public lands domain: NPS comments about vehicle clearance rules (a routine, low-salience matter) score 5%, while BLM comments about Trump administration rescissions of conservation rules (a high-salience political matter) score 31%.

A longitudinal analysis reinforces this interpretation. Across six agencies sampled at multiple points between 2019 and 2025, AI scores were indistinguishable from zero before November 2022 (ChatGPT's launch) and rise sharply to 17–20% by 2025 in politically contested domains (USCIS, IRS, CMS, BLM). The NPS public lands series — a low-salience control — remains near zero throughout. The technology is constant; the adversarial context drives adoption.

---

## 2. Background and Related Work

**The notice-and-comment process.** Under 5 U.S.C. § 553, federal agencies must publish proposed rules in the Federal Register, accept written comments from the public during a designated comment period (typically 30–60 days), and respond to significant comments in the final rule's preamble. Agencies are not required to follow the majority view, but courts review whether agencies "considered" public input. This creates an incentive for organized interest groups to flood dockets with comments supporting their preferred outcome — a practice sometimes called "comment bombing."

**AI in political communication.** Decker (2026) provides the closest analog to this study. Analyzing floor speeches and press releases from members of Congress, Decker finds that AI adoption has increased sharply since 2023, with junior members and those with heavier workloads showing the highest adoption. The present paper applies similar methods to citizen-facing regulatory comments, a context where adoption patterns may differ substantially: citizens face lower reputational costs from AI use than elected officials, but also have less professional capacity to integrate AI tools into their workflow.

**AI detection methodology.** I use the Pangram AI detection API (v3), which returns `fraction_ai`, a continuous score from 0 to 1 measuring the probability that a text was fully AI-generated. Pangram also returns `fraction_ai_assisted`, capturing text that was partially AI-edited. Calibration tests confirm the detector works as expected on the text types in this study: a human comment with spelling errors scores 0.0, while a prompt-generated comment on the same topic scores 1.0.

A key limitation of AI detection is that detectors are calibrated on specific text genres. Prior work on court opinions (which use dense legal citation) and academic papers (which use technical jargon) finds near-zero AI scores even for post-ChatGPT text. The present study focuses on public comments — a genre closer to consumer reviews and advocacy letters, which AI detectors handle reliably.

---

## 3. Data

**Comment collection.** I collect public comments from Regulations.gov using the API v4. I identify active 2025 dockets across sixteen agencies, sample up to 50 unique comments per agency, and filter to comments with at least 50 words (to exclude attachment-only stubs). Duplicate form letters are removed using a fingerprint of the first 15 words. The final dataset contains 498 scored comments.

**Agencies and dockets.** The sixteen agencies span six thematic categories:

| Agency | Category | Docket Topic | N |
|--------|----------|-------------|---|
| FHWA | Political/environment | NEPA regulations revision | 10 |
| BLM | Political/environment | Rescission of conservation rules | 71 |
| USCIS | Political/immigration | Alien registration requirements | 106 |
| HRSA | Health policy | 340B drug pricing rebate model | 40 |
| FinCEN | Finance | Financial crime enforcement | 20 |
| IRS | Finance | Tax rules | 33 |
| FTC | Finance | Competition rules | 20 |
| OCC | Finance | Banking rules | 3 |
| WHD | Labor | Wage and hour rules | 38 |
| ETA | Labor | Employment training | 50 |
| DOL | Labor | Labor regulations | 20 |
| EBSA | Labor | Retirement benefits | 6 |
| OSHA | Labor | Workplace safety | 11 |
| NPS | Routine/public lands | National parks vehicle rules | 40 |
| APHIS | Agriculture | Wildlife management | 23 |
| USDA | Agriculture | Agriculture rules | 7 |

**AI scoring.** Each comment is scored with Pangram v3. I cap text at 5,000 words to manage API costs. Total scoring cost: approximately $6 in API credits. I use `fraction_ai` as the primary outcome variable throughout.

---

## 4. Results

### 4.1 Overall Prevalence

AI-generated content is detectable in 18.3% of comments (91 of 498 with scores above 0.1). The mean AI score across all comments is 0.183. This is not noise: the detector confidently assigns scores of 1.0 to the majority of flagged comments, and the distribution is bimodal (mass at 0 and mass near 1.0), consistent with a mixture of fully human and fully AI-generated text rather than a continuum of AI-assisted writing.

AI-generated comments are meaningfully longer: the average AI-scored comment (score > 0.5) contains 259 words, compared to 182 words for human-written comments — a 42% difference. This is consistent with the hypothesis that AI removes the friction of writing a longer, more structured argument.

### 4.2 Cross-Agency Variation

Table 1 presents mean AI scores by agency, sorted by adoption rate.

**Table 1: AI Adoption by Agency (2025)**

| Agency | Category | N | Mean AI Score | % Score > 0.1 |
|--------|----------|---|--------------|--------------|
| FHWA | Political/environment | 10 | 0.400 | 40.0% |
| HRSA | Health policy | 40 | 0.400 | 40.0% |
| BLM | Political/environment | 71 | 0.296 | 30.9% |
| USCIS | Political/immigration | 106 | 0.236 | 23.6% |
| FinCEN | Finance | 20 | 0.200 | 20.0% |
| EBSA | Labor | 6 | 0.167 | 16.7% |
| WHD | Labor | 38 | 0.132 | 13.2% |
| IRS | Finance | 33 | 0.121 | 12.1% |
| ETA | Labor | 50 | 0.100 | 10.0% |
| OSHA | Labor | 11 | 0.091 | 9.1% |
| FTC | Finance | 20 | 0.050 | 5.0% |
| NPS | Routine/public lands | 40 | 0.050 | 5.0% |
| APHIS | Agriculture | 23 | 0.043 | 4.3% |
| DOL | Labor | 20 | 0.000 | 0.0% |
| USDA | Agriculture | 7 | 0.000 | 0.0% |

*Notes: AI score from Pangram v3, range [0,1]. Comments with fewer than 50 words excluded. Duplicate form letters removed. OCC (n=3) omitted for insufficient sample. All flagged agencies have at least one comment scoring 1.0.*

The range is striking: BLM (0.296) is six times NPS (0.050), despite both being public lands agencies receiving comments from similar populations of outdoor enthusiasts and conservation advocates. HRSA's 340B drug pricing docket (0.400) and FHWA's NEPA rollback docket (0.400, n=10) top the table, though the FHWA estimate carries wide confidence intervals given the small sample.

**Category-level summary.** Collapsing agencies into six categories:

- Health policy: mean AI = **0.400**
- Political/environment: mean AI = **0.309**
- Political/immigration: mean AI = **0.236**
- Finance/compliance: mean AI = **0.132**
- Labor: mean AI = **0.096**
- Routine public lands: mean AI = **0.050**
- Agriculture: mean AI = **0.033**

### 4.3 The NPS vs. BLM Natural Experiment

The starkest comparison in the data is between NPS and BLM. Both are public lands agencies. Both attract comments from similar populations — hikers, hunters, conservationists. Both dockets were open in 2025. The difference:

- **NPS-2025-0001/0003**: Rules governing vehicle clearance requirements on Assateague Island National Seashore — a routine, technical, low-salience matter affecting off-road vehicle enthusiasts. Mean AI score: **0.050**.
- **BLM-2025-0001/0002**: Rules rescinding Obama/Biden-era conservation rules protecting public lands — a high-salience political matter that attracted national media coverage and organized advocacy campaigns. Mean AI score: **0.296**.

This comparison controls for agency ecosystem (public lands), commenter population (outdoor enthusiasts), year (2025), and technology availability. The only thing that varies is political salience. The six-fold difference in AI adoption is difficult to explain by anything other than the adversarial mobilization that high-salience political rules generate.

A second high-AI docket — FHWA's revision of NEPA environmental review regulations (0.400, n=10) — reinforces this interpretation. NEPA rollbacks are among the most contested environmental policy actions of the Trump administration, attracting organized opposition from environmental groups. The same adversarial dynamic that drives AI use on BLM conservation rules appears to apply here, though the small FHWA sample warrants caution.

### 4.4 The Health Policy Anomaly

HRSA's 340B drug pricing rebate model pilot (mean AI = 0.400) is the highest-scoring agency in the dataset with an adequate sample, and it does not fit cleanly into the grassroots political mobilization story. The 340B program, which requires drug manufacturers to provide discounted medications to safety-net hospitals and clinics, has become a battleground between pharmaceutical companies seeking rebate-model reforms and hospital associations defending the existing discount structure. The high AI score on this docket likely reflects organized industry stakeholder commenting — law firms, trade associations, and healthcare systems generating polished policy arguments at scale — rather than citizen advocacy campaigns.

This distinction matters for interpretation. Grassroots AI use (BLM, USCIS) inflates apparent public sentiment. Industry AI use (HRSA) potentially drowns out the authentic voices of the safety-net providers and patients the program is designed to serve. Both distort the notice-and-comment process, but through different mechanisms.

### 4.5 Temporal Trends: AI Adoption Since ChatGPT

To test whether AI adoption tracks ChatGPT's November 2022 release, I construct a longitudinal panel by sampling up to 40 comments per agency-year from six agencies (USCIS, NPS, IRS, CMS, BLM, EPA) across 2019–2025. Comments are drawn from the full comment stream for each agency in each year using random page sampling across Regulations.gov. I retain agency-year cells with at least ten scored observations; 18 cells meet this threshold across the six agencies.

**Figure 3** plots mean AI score by agency and year. The result is striking: every series is indistinguishable from zero before 2023, and four of the five series with 2025 data show AI adoption rates of 16–20% in 2025. The one exception is NPS (routine public lands), which reaches only 5% — consistent with its low cross-sectional score in the 2025 dataset.

The post-2022 inflection is visible across all contested-domain agencies regardless of policy area: immigration (USCIS), finance (IRS), health (CMS), and environment (BLM) all show the same pattern. This cross-domain simultaneity is consistent with a supply-side shock (ChatGPT making generation easy) interacting with pre-existing adversarial incentives, rather than any docket-specific factor.

EPA provides an informative methodological note: its comment stream is dominated by organizational PDF attachments, with fewer than 5% of 2025 comments containing inline text above the 50-word threshold. This is consistent with EPA's commenter base being professional and institutional rather than citizen-driven. The EPA series ends at 2022 (n=40, mean=0.000) in Figure 3 not because EPA 2025 has low AI adoption, but because its comment format makes detection infeasible with this method.

**The 2025 political context.** The scale of the 2025 surge — from roughly 4% in 2024 to 16% pooled across agencies — warrants a separate interpretive note. The Trump administration's first months in office produced an unusually dense portfolio of high-salience, contested rulemakings: alien registration requirements, conservation land rescissions, Medicaid work requirements, offshore energy leasing, and sweeping NEPA rollbacks, all opened for public comment within a compressed window. This created an unusually high density of adversarial mobilization opportunities simultaneously. Two mechanisms may be operating at once. First, AI tools have simply become easier to use and more widely known since 2023, producing secular diffusion. Second, the political moment generated organized advocacy campaigns in which AI-drafted templates were distributed to supporters — a supply-side shock to AI comment volume that is specific to this administration's regulatory agenda. The panel data cannot fully distinguish these mechanisms: both predict rising AI adoption in 2025, and the cross-domain simultaneity (immigration, health, environment, finance all rising together) is consistent with both. Disentangling secular diffusion from adversarial mobilization will require docket-level analysis of whether comments cluster around specific template phrases — a promising extension left to future work.

### 4.6 What Do AI-Generated Comments Look Like?

Qualitative review of the top AI-scored USCIS comments reveals three distinct patterns of AI use:

**Pattern 1: Mass-individualized advocacy campaigns.** Multiple comments on the alien registration rule share the same structural argument (historical parallel to wartime registration, call for rescission, concern for undocumented families) but with different phrasings. No personal stories, no individual details. Example:

> *"I strongly oppose the Interim Final Rule on Alien Registration... It reminds us of some of the worst moments in U.S. and world history when people were forced to register based on their race or nationality, leading to punishment and discrimination."* (USCIS-2025-0004-3769, 160 words, AI score: 1.0)

This pattern suggests advocacy organizations are using AI to generate individualized comment variations at scale — specifically to defeat agencies' practice of dismissing identical duplicate submissions.

**Pattern 2: AI-structured policy arguments.** Some comments use GPT's characteristic header-then-explanation format to organize multiple policy objections:

> *"Intrusion of Privacy: Reviewing someone's social media raises significant privacy concerns... Potential for Misuse: There is the risk that immigration officers may overstep boundaries... Contextual Misinterpretation: Social media posts can be taken out of context..."* (USCIS-2025-0003-0279, 332 words, AI score: 1.0)

**Pattern 3: AI as policy translator.** A small subset of high-scoring comments appear to reflect genuine individual concern expressed through AI assistance — someone who asked ChatGPT to help them articulate a specific technical argument:

> *"I oppose the collection of social media identifiers due to significant security vulnerabilities... Bad actors could create fraudulent social media platforms specifically targeting potential immigrants. Once users register on these platforms, automated systems could generate millions of associated handles."* (USCIS-2025-0003-0174, 167 words, AI score: 1.0)

This argument is specific, plausible, and novel — it addresses an angle not covered in advocacy talking points. It likely represents an individual who used AI to help articulate a concern they genuinely hold. This is qualitatively different from form-letter generation, and raises distinct normative questions.

---

## 5. Discussion

### 5.1 Adversarial Mobilization, Not Diffusion

The standard account of technology adoption in politics follows a diffusion model: new tools spread gradually as awareness increases, costs decline, and norms shift. If that model applied here, we would expect AI adoption to be roughly uniform across agencies and rule types, with variation driven primarily by commenter sophistication (organizations vs. individuals, educated vs. not).

The data tells a different story. AI adoption is concentrated in politically adversarial contexts — rules where citizens are fighting the government on high-salience policy questions. The technology is equally available to commenters on USDA agriculture rules and BLM conservation rescissions. The difference is incentive. When the stakes are high and the relationship is adversarial, citizens and advocacy organizations reach for tools that make their comments more persuasive, more voluminous, and harder to dismiss.

This pattern is consistent with the broader literature on political mobilization, which finds that participation intensity tracks perceived threat rather than baseline civic engagement. The BLM and USCIS dockets in 2025 attracted massive comment volumes (61,637 and 5,400+ respectively) because they represented high-salience threats to communities — public lands users and immigrant communities — who mobilized in response. AI was one of the tools they used.

The HRSA finding suggests a second mechanism: organized professional stakeholder mobilization. The 340B drug pricing rule is technically complex and financially significant, attracting sophisticated institutional commenters (hospitals, insurers, trade associations) who have the capacity and incentive to deploy AI tools to generate high-volume, high-quality comments. Adversarial mobilization thus appears to operate at two levels: grassroots citizen campaigns and coordinated institutional campaigns.

### 5.2 Implications for the Notice-and-Comment Process

The notice-and-comment process rests on an implicit theory of democratic participation: individual citizens, each expressing their authentic preferences, provide agencies with information about who is affected by a proposed rule and how. Agencies aggregate this information alongside technical expertise to reach a reasoned decision.

AI-generated comments challenge this theory in at least two ways.

First, *volume inflation*. If advocacy organizations use AI to generate thousands of individually-varied comments that express the same underlying position, agencies face a distorted signal about the breadth of public concern. The 139,757 comments on BLM-2025-0002 may represent a much smaller number of distinct viewpoints, inflated by AI generation.

Second, *voice substitution*. When a citizen uses AI to generate a comment on their behalf, whose voice is being submitted? The commenter's genuine concern (as in Pattern 3 above) or the AI's synthesis of policy arguments? This matters if agencies give more weight to comments that reflect lived experience — the "I have been an immigration attorney for 14 years" comment is treated differently than the "I strongly oppose" template. AI may systematically shift the observable distribution of comment types away from personal testimony and toward polished policy argument.

### 5.3 Limitations

Several limitations constrain interpretation of these results. First, the cross-sectional sample covers 16 agencies and 498 comments; the patterns should be replicated at larger scale before drawing strong conclusions. Second, AI detection is imperfect — Pangram may miss some AI-generated content (false negatives) and may occasionally flag human writing as AI-generated (false positives), though calibration tests suggest the latter is rare. Third, I cannot observe the full distribution of comments on each docket, only the sample I collected; sampling variation may affect agency-level estimates, particularly for agencies with small samples (FHWA n=10, OCC n=3, USDA n=7). Fourth, I cannot distinguish citizen AI use from institutional AI use within a docket; the HRSA finding likely reflects industry stakeholders, but this cannot be confirmed from comment text alone. Fifth, the longitudinal panel (Figure 3) has uneven coverage — several agency-year cells fall below the n=10 threshold due to API rate limits and the prevalence of attachment-only submissions, particularly at EPA — so the time-series estimates should be interpreted as indicative rather than definitive.

---

## 6. Conclusion

I find that AI-generated content is detectable in 18.3% of 2025 public comments to federal agencies, with adoption ranging from near-zero for routine technical rules (USDA, DOL) to 40% for high-stakes contested rules (HRSA, FHWA). The BLM vs. NPS comparison — same agency ecosystem, same commenter population, same year — provides compelling evidence that political salience rather than technological availability drives AI adoption. The HRSA finding extends this logic to institutional stakeholder campaigns, suggesting AI is deployed wherever the adversarial stakes are high — whether those stakes are political or financial.

These findings have practical implications for administrative law. Agencies currently count comments and weight them by apparent quality and specificity. If AI allows advocacy organizations to simultaneously inflate comment volume and increase apparent quality, the notice-and-comment process may be systematically skewed toward well-organized interests that deploy AI at scale. Whether this represents a democratic crisis or a democratizing force — helping ordinary citizens articulate concerns they couldn't express alone — depends on which of the three patterns of AI use dominates in practice.

---

## References

Administrative Procedure Act, 5 U.S.C. § 553 (1946).

Decker, A. (2026). Who uses AI in Congress? *Working Paper.*

Executive Order 12866, Regulatory Planning and Review (1993).

Pangram Labs. (2025). Pangram AI Detection API v3. text.api.pangram.com.

Regulations.gov API v4. api.regulations.gov/v4.

---

*Data and replication code available at: [github link]*
