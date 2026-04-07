# Artificial Advocacy: AI-Generated Public Comments and the Future of Notice-and-Comment Rulemaking

**Stevie Miller[^*]**

[^*]: The author thanks Pratik Sachdeva for valuable comments. Data and replication code are available at https://github.com/stevie-ml/ai-public-comments.

## Abstract

This Article provides the first systematic empirical measurement of AI-generated content in federal public comments submitted through Regulations.gov. Using a validated AI detection instrument, I score 5,326 comments across eighteen federal agencies from 2019 to 2025 and find that 18.3% of 2025 comments contain detectable AI-generated content. But this aggregate figure conceals dramatic variation: AI adoption ranges from near-zero for routine technical rules to 40% for politically contested and financially significant rulemakings. A natural experiment comparing two public lands agencies — the Bureau of Land Management (30.9% AI) and the National Park Service (5.0% AI) — in the same year, with similar commenter populations, demonstrates that political salience rather than technological availability drives adoption. A longitudinal panel confirms that AI scores were indistinguishable from zero before ChatGPT's November 2022 launch and rose sharply thereafter, but only in adversarial regulatory contexts. AI-generated comments are disproportionately left-leaning in rhetorical framing, amplify the dominant position within each docket, and score slightly higher on argument quality than human-written comments — raising the specter of AI-powered advocacy that is simultaneously more polished and less authentic than the citizen participation the Administrative Procedure Act was designed to facilitate. I argue that the notice-and-comment process, as currently administered, lacks the institutional capacity to distinguish genuine public sentiment from AI-inflated advocacy, and I propose a framework of disclosure requirements, detection-assisted processing, and revised judicial review standards to preserve the democratic legitimacy of informal rulemaking in an era of generative AI.

---

## Introduction

The notice-and-comment process is "one of the greatest inventions of modern government."[^1] Under section 553 of the Administrative Procedure Act ("APA"),[^2] federal agencies must publish proposed rules in the Federal Register, invite written comments from the public, and "consider" those comments before issuing final rules.[^3] Courts enforce this obligation vigorously: the D.C. Circuit has vacated agency action for failing to respond to "significant" comments,[^4] and the Supreme Court in *Motor Vehicle Manufacturers Ass'n v. State Farm Mutual Automobile Insurance Co.* established that agency rulemaking must reflect "reasoned decisionmaking" informed by the administrative record — a record that centrally includes public comments.[^5]

The legitimacy of this process rests on an assumption so fundamental that it is rarely stated: that comments submitted to federal dockets represent authentic expressions of human judgment. An agency reading a comment is supposed to be reading the views of a person — a farmer worried about pesticide regulation, a hospital administrator explaining how a payment rule affects patient care, a small business owner objecting to a compliance burden. The APA's framers could not have anticipated a technology that would allow any person, or any organization, to generate thousands of individually varied, substantively detailed public comments at negligible marginal cost.

That technology now exists. Since the release of ChatGPT in November 2022, large language models ("LLMs") have made it trivially easy to produce polished prose on any topic.[^6] A citizen who previously might have submitted "please don't do this, it's bad for my community" can now prompt an AI to generate a 300-word argument citing regulatory history, constitutional concerns, and economic impacts. An advocacy organization that once spent staff time drafting a single form letter for supporters to sign can now generate thousands of individually varied versions — each different enough to evade agencies' duplicate-detection filters, yet each expressing the same underlying position.

This Article asks three questions. First, how prevalent is AI-generated content in federal public comments? Second, what drives variation in AI adoption across regulatory contexts? Third, what are the legal implications for the notice-and-comment process, and what should agencies, courts, and Congress do about it?

To answer the first two questions, I construct a novel dataset of 5,326 public comments from eighteen federal agencies spanning 2019 to 2025, scored with a validated AI detection instrument. My central empirical finding is that AI adoption in public comments is not a story of gradual technological diffusion. It is a story of *adversarial mobilization*. AI-generated content is concentrated in politically contested and financially high-stakes rulemakings — immigration enforcement, public lands conservation, drug pricing — and is virtually absent from routine technical dockets. The technology is equally available to all commenters; the difference is incentive. When the stakes are high and the relationship between citizens and the government is adversarial, organized interests reach for AI as a force multiplier.

To answer the third question, I draw on administrative law doctrine — particularly the APA's procedural requirements, the "hard look" standard of judicial review, and the evolving case law on mass and form-letter comments — to argue that AI-generated comments create a novel challenge that existing legal frameworks are ill-equipped to handle. Unlike traditional form-letter campaigns, which agencies have long managed by counting as a single expression of a shared view,[^7] AI-generated comments are designed to appear individually authored. They defeat the heuristics agencies use to distinguish genuine public input from organized advocacy. And because AI amplifies whichever side of a regulatory debate deploys it, agencies cannot simply discount AI-generated comments without making the kind of substantive judgment about comment content that the APA's procedural neutrality is designed to prevent.

This Article proceeds in six Parts. Part I describes the legal framework governing notice-and-comment rulemaking and the challenges that mass comments have historically posed. Part II explains the AI detection methodology and presents a validation study demonstrating its reliability. Part III describes the data. Part IV presents the empirical results. Part V analyzes the ideological dimensions of AI-generated comments. Part VI proposes a legal framework for preserving the integrity of the notice-and-comment process.

---

## I. The Legal Framework

### A. Notice-and-Comment Under the APA

The APA's notice-and-comment requirement, codified at 5 U.S.C. § 553, is deceptively simple. After publishing a notice of proposed rulemaking ("NPRM") in the Federal Register, an agency must "give interested persons an opportunity to participate in the rule making through submission of written data, views, or arguments."[^8] The agency must then "consider" the "relevant matter presented"[^9] and include in the final rule "a concise general statement of [its] basis and purpose."[^10]

Courts have given this spare statutory text considerable doctrinal elaboration. The D.C. Circuit's "reasoned decisionmaking" requirement, rooted in *State Farm* and its progeny, demands that agencies engage meaningfully with significant comments.[^11] An agency that ignores a well-supported objection to its proposed rule risks reversal on judicial review.[^12] In *United States v. Nova Scotia Food Products Corp.*, the Second Circuit held that the "concise general statement" must respond to "the major comments" and demonstrate that the agency has "genuinely engaged in reasoned decision-making."[^13]

The theoretical justification for notice-and-comment has been debated extensively in the administrative law literature. Professor Nina Mendelson has argued that public comments serve an informational function — providing agencies with data about on-the-ground conditions that they would not otherwise possess — and a legitimacy function — ensuring that affected parties have a voice in the rules that govern them.[^43] Professor Cary Coglianese has emphasized the epistemic value of comments: even when individual comments lack technical sophistication, they can alert agencies to practical implementation problems, unintended consequences, and distributional effects that technical analysis alone would miss.[^44] Professors Michael Livermore and Richard Revesz have gone further, developing quantitative methods for analyzing comment content and arguing that systematic analysis of public comments can reveal patterns of public preference that should inform agency decisionmaking.[^45]

These accounts share a common premise: that public comments convey *information* — about facts, preferences, or practical consequences — that originates with the commenter. The informational value of a comment from a small business owner describing how a proposed rule would affect her operations depends on the comment reflecting her actual experience. If the comment instead reflects an AI model's synthesis of generic policy arguments, the informational signal is fundamentally different: the agency is learning about what a language model predicts a person *might* say, not about what a person actually knows.

Crucially, the APA does not require agencies to follow the majority view expressed in public comments. Rulemaking is not a plebiscite.[^14] As the D.C. Circuit emphasized in *Action on Smoking and Health v. CAB*, an agency "need not conduct a plebiscite" and may reject the position supported by the majority of commenters if it provides a reasoned explanation.[^15] But agencies must *consider* the substance of comments, and courts have interpreted this obligation to require, at minimum, that agencies acknowledge and respond to significant points raised by commenters.[^16] In *Perez v. Mortgage Bankers Ass'n*, the Supreme Court reaffirmed that the notice-and-comment process serves as a "vital check" on agency power, underscoring the importance of genuine public participation in maintaining the legitimacy of the administrative state.[^46]

This doctrinal framework creates an important asymmetry. Agencies are legally obligated to read and respond to substantive comments, but they are not required to verify that those comments were written by the persons who submitted them. Nothing in the APA requires that a comment reflect the commenter's own words, analysis, or experience. A law firm drafting a comment for a trade association client is indistinguishable, in the eyes of the APA, from a farmer writing in her own words. The statute regulates the *agency's* obligation to consider, not the *commenter's* obligation to be authentic. This gap — between the APA's procedural requirements and its implicit assumption of human authorship — is the space in which AI-generated comments operate.

### B. The Mass Comment Problem

The challenge of mass and form-letter comments predates AI by decades. As Regulations.gov made it easier for advocacy organizations to mobilize supporters, agencies began receiving comment volumes that far exceeded their capacity for individual review. The EPA's 2014 Clean Power Plan received over four million comments.[^17] The FCC's 2017 net neutrality proceeding received over twenty-two million — many of them later revealed to be fraudulent submissions using stolen identities.[^18]

Agencies have developed informal practices for managing mass comments. When thousands of comments share identical or near-identical text, agencies typically treat them as a single expression of a shared viewpoint and respond to the substance once.[^19] The D.C. Circuit has endorsed this approach: in *American Mining Congress v. EPA*, the court held that agencies need not respond individually to each of thousands of postcards expressing the same view.[^20] What matters is that the agency addresses the *substance* of the concern, not that it counts votes.

The Administrative Conference of the United States ("ACUS") formalized this approach in its 2021 recommendation on managing mass, computer-generated, and fraudulent comments.[^47] ACUS recommended that agencies develop procedures for identifying and grouping duplicative comments, deploy technological tools to assist in comment analysis, and focus analytical resources on comments that raise "novel factual, scientific, or legal issues."[^48] The recommendation explicitly contemplated the possibility that comments might be generated by automated systems, but its proposed solutions — duplicate detection, clustering, and keyword analysis — assumed that automated comments would be textually identical or near-identical to other comments in the same campaign.

The FCC's experience with the 2017 net neutrality proceeding illustrates both the scale of the problem and the limitations of existing responses. The proceeding received over twenty-two million comments — more than any federal rulemaking in history.[^18] A subsequent investigation by the New York Attorney General revealed that millions of these comments were fraudulent: submitted using real Americans' stolen identities by a broadband industry group that paid a lead-generation firm to manufacture the appearance of grassroots opposition to net neutrality rules.[^49] The campaign used simple text templates with minor word substitutions — a crude precursor to the AI-individualized advocacy documented in this Article. Despite the Attorney General's findings, the FCC processed all comments, including the fraudulent ones, and the D.C. Circuit in *Mozilla Corp. v. FCC* did not require the agency to have detected or excluded the fraudulent submissions.[^50] The legal system, in other words, treated millions of fake comments as a regrettable but legally irrelevant feature of the administrative record.

This framework worked tolerably well in the era of copy-paste form letters. An advocacy group would draft a template comment, distribute it to supporters, and thousands of identical or near-identical submissions would arrive at the agency. The agency could identify these as form letters, group them, and respond to the shared argument once. Professor Stuart Benjamin has documented how agencies developed increasingly sophisticated text-matching tools to manage this process, and how advocacy groups responded by encouraging supporters to add personal sentences to template comments — an early arms race between detection and evasion that foreshadowed the AI challenge.[^51]

AI disrupts this equilibrium fundamentally. A form-letter campaign powered by AI does not produce thousands of identical comments. It produces thousands of *individually varied* comments that make the same argument in different words, with different structures, and sometimes with different supporting points. From the agency's perspective, each comment appears to be an independent expression of an individual viewpoint. The duplicate-detection heuristics that agencies have relied on for decades — including the ACUS-recommended clustering tools — are useless against AI-individualized advocacy. The arms race between advocacy groups and agencies has tilted decisively in favor of the advocates.

### C. Judicial Review and the "Hard Look" Doctrine

The "hard look" doctrine, developed primarily by the D.C. Circuit in cases like *Greater Boston Television Corp. v. FCC*[^21] and codified in the Supreme Court's *State Farm* framework, requires courts to examine whether the agency engaged in reasoned decisionmaking. Under this standard, a court must determine whether the agency "examine[d] the relevant data and articulate[d] a satisfactory explanation for its action including a rational connection between the facts found and the choice made."[^22]

For AI-generated comments, the hard look doctrine creates a dilemma. If an agency fails to respond to a substantive argument raised in an AI-generated comment, a reviewing court might find the agency's decisionmaking arbitrary and capricious — even if the argument was manufactured by an advocacy group using AI rather than developed by an individual commenter based on personal experience or expertise. Conversely, if an agency detects that comments are AI-generated and discounts them for that reason, it risks a different form of arbitrary and capricious review: the agency would be making a judgment about the *provenance* rather than the *substance* of the comment, which finds no support in the APA's text or in existing case law.

This Article argues that this dilemma is not merely hypothetical. As AI-generated comments become more prevalent and more sophisticated, agencies will increasingly face records dominated by machine-generated text. The legal framework must evolve to address this reality.

---

## II. Methodology: Detecting AI-Generated Text

### A. The Pangram AI Detection Instrument

I use the Pangram AI detection API (version 3), a commercial text classifier that returns a continuous score from 0.0 to 1.0 measuring the probability that a given text was fully AI-generated.[^23] Pangram also returns a separate `fraction_ai_assisted` score capturing text that was partially edited or enhanced by AI. I use the `fraction_ai` score as the primary outcome variable throughout this Article.

A key limitation of AI detection is genre dependence. Detectors are trained on specific text types, and their accuracy varies across genres.[^24] Prior work on court opinions — which use dense legal citation and formulaic structure — finds that AI detectors produce unreliable results.[^25] Public comments, however, occupy a textual genre closer to consumer reviews, opinion editorials, and advocacy letters — genres on which modern AI detectors achieve high accuracy.[^26]

### B. Validation Study

To validate Pangram's performance on the specific text genre at issue — federal public comments — I conduct a controlled experiment. I assemble three sets of comments:

1. **Human baseline (n = 25).** Real public comments submitted in 2018, before the existence of any modern LLM. These comments are definitionally human-written and serve as the ground truth for the zero-AI condition.

2. **Claude-generated (n = 25).** Comments generated by Anthropic's Claude (Opus 4.6) on matched topics. For each human comment, I generate an AI comment on the same regulatory topic and of similar length.

3. **GPT-5-generated (n = 25).** Comments generated by OpenAI's GPT-5 on the same matched topics, testing whether Pangram's detection is model-agnostic.

All seventy-five comments are scored with Pangram v3. The results are striking:

**Table 1: Pangram Validation Results**

| Source | N | Mean AI Score | Correctly Classified | False Rate |
|--------|---|--------------|---------------------|------------|
| Human (2018) | 25 | 0.000 | 25/25 (100%) | 0% FP |
| Claude (Opus 4.6) | 25 | 0.920 | 23/25 (92%) | 8% FN |
| GPT-5 | 25 | 1.000 | 25/25 (100%) | 0% FN |
| **Overall** | **75** | — | **73/75 (97.3%)** | — |

Pangram achieves 97.3% balanced accuracy with zero false positives. No human comment is incorrectly flagged as AI-generated. Two Claude-generated comments — both short, topically simple comments about national park airstrip access — score below the 0.5 threshold and are misclassified as human. GPT-5-generated comments are detected with perfect accuracy, and every GPT-5 comment scores 1.0. The detector is model-agnostic: it identifies AI-generated text from both major model families with high reliability.

The zero false positive rate is particularly important for this study. Because I am using AI detection to make claims about the prevalence and distribution of AI-generated comments in the wild, false positives — incorrectly labeling human comments as AI-generated — would inflate prevalence estimates and potentially distort cross-agency comparisons. The validation study suggests this risk is minimal.

---

## III. Data

I construct two datasets from Regulations.gov using the API v4.

**Cross-sectional dataset.** I collect comments from active 2025 dockets across sixteen agencies spanning seven thematic categories: political/environment (BLM, FHWA), political/immigration (USCIS), health policy (HRSA), finance (IRS, FinCEN, FTC, OCC), labor (WHD, ETA, DOL, EBSA, OSHA), routine public lands (NPS), and agriculture (APHIS, USDA). I sample up to fifty unique comments per agency, filtering to comments with at least fifty words and removing duplicate form letters using a fingerprint of each comment's first fifteen words. The final dataset contains 498 scored comments.

**Full panel dataset.** For the expanded analysis, I sample up to sixty-five comments per agency-year cell across eighteen agencies and seven years (2019–2025), using full-range random page sampling and docket stratification to ensure representativeness.[^27] This yields 5,326 scored comments — the largest AI-detection dataset applied to federal public comments to date.

**LLM classification subsample.** To analyze the political content of AI-generated comments, I classify a subsample of 414 comments using Claude Haiku as an automated coder.[^28] The subsample includes all 138 comments scoring 1.0 (fully AI-generated) and a stratified random sample of 276 comments scoring 0.0 (fully human-written), matched by regulatory category. Each comment is classified on four dimensions: regulatory stance (pro- or anti-regulation), ideological framing (left or right), argument type (technical, emotional, form letter, or substantive-novel), and argument quality (1–5 scale).

---

## IV. Results

### A. Overall Prevalence

AI-generated content is detectable in 18.3% of 2025 public comments (91 of 498 with scores above 0.1). The distribution is bimodal: comments cluster at 0.0 (fully human) or near 1.0 (fully AI-generated), with little mass in between. This pattern is consistent with a mixture of two populations — commenters who use AI and commenters who do not — rather than a continuum of AI-assisted writing.

AI-generated comments are meaningfully longer than human-written comments. The average AI-scored comment (score > 0.5) contains 259 words, compared to 182 words for human-written comments — a 42% difference (log word count coefficient = 0.094, p < 0.001 in regression specifications with category fixed effects). This is consistent with the hypothesis that AI removes the friction of producing longer, more structured arguments.

### B. Cross-Agency Variation

The aggregate prevalence figure conceals dramatic variation across regulatory context. Table 2 presents mean AI scores by agency.

**Table 2: AI Adoption by Agency (2025)**

| Agency | Category | N | Mean AI Score | % Flagged |
|--------|----------|---|--------------|-----------|
| FHWA | Political/environment | 10 | 0.400 | 40.0% |
| HRSA | Health policy | 40 | 0.400 | 40.0% |
| BLM | Political/environment | 71 | 0.296 | 30.9% |
| USCIS | Political/immigration | 106 | 0.236 | 23.6% |
| FinCEN | Finance | 20 | 0.200 | 20.0% |
| WHD | Labor | 38 | 0.132 | 13.2% |
| IRS | Finance | 33 | 0.121 | 12.1% |
| ETA | Labor | 50 | 0.100 | 10.0% |
| NPS | Routine/public lands | 40 | 0.050 | 5.0% |
| APHIS | Agriculture | 23 | 0.043 | 4.3% |
| DOL | Labor | 20 | 0.000 | 0.0% |
| USDA | Agriculture | 7 | 0.000 | 0.0% |

The range is an order of magnitude: HRSA and FHWA (0.400) versus USDA and DOL (0.000). Regression analysis with heteroskedasticity-consistent standard errors confirms that regulatory category is a strong predictor of AI adoption. Relative to the agriculture baseline, health policy comments show a 0.357 increase in AI score (p < 0.001), political/environment comments a 0.270 increase (p < 0.001), and political/immigration comments a 0.206 increase (p < 0.001). Routine public lands and labor categories are not statistically distinguishable from agriculture.

### C. The NPS–BLM Natural Experiment

The starkest comparison in the data exploits a natural experiment within the public lands regulatory ecosystem. Both the National Park Service and the Bureau of Land Management are Department of the Interior agencies. Both attract comments from similar populations — hikers, hunters, anglers, conservationists. Both had active 2025 dockets. The difference lies entirely in political salience:

- **NPS-2025-0001/0003**: Rules governing vehicle clearance requirements on Assateague Island National Seashore — a routine, technical, low-salience matter affecting off-road vehicle enthusiasts. Mean AI score: **0.050**.
- **BLM-2025-0001/0002**: Rules rescinding Obama- and Biden-era conservation rules protecting public lands from energy development — a high-salience political matter that attracted national media coverage, organized advocacy campaigns, and over 139,000 total comments. Mean AI score: **0.296**.

This comparison controls for agency ecosystem, commenter population, year, and technology availability. The only dimension of variation is political salience. The six-fold difference in AI adoption rates provides compelling quasi-experimental evidence for the adversarial mobilization hypothesis.

### D. The Health Policy Anomaly

HRSA's 340B drug pricing rebate model pilot (mean AI = 0.400) is the highest-scoring docket with an adequate sample, and it challenges a simple "grassroots mobilization" narrative. The 340B program requires drug manufacturers to provide discounted medications to safety-net hospitals and clinics. It has become a battleground between pharmaceutical companies seeking rebate-model reforms and hospital associations defending the existing discount structure.[^29]

The high AI score on this docket likely reflects organized *industry* stakeholder commenting — law firms, trade associations, and hospital systems generating polished policy arguments at scale — rather than citizen advocacy campaigns. This distinction matters: grassroots AI use (BLM, USCIS) inflates apparent public sentiment, while industry AI use (HRSA) potentially drowns out the authentic voices of safety-net providers and patients the program serves. Both distort the notice-and-comment process, but through different mechanisms and with different distributional consequences.

### E. Temporal Trends

To test whether AI adoption tracks the post-ChatGPT inflection point documented in other domains,[^30] I use the full panel dataset of 5,326 comments spanning 2019–2025 across eighteen agencies.

The aggregate trend is striking. Mean AI scores were effectively zero from 2019 through 2021 (0.3%, 0.1%, and 0.0% respectively). A small uptick appears in 2022 (0.5%), coinciding with the launch of ChatGPT in November of that year. The first substantial jump occurs in 2023 (9.5%), a tenfold increase that corresponds to the rapid diffusion of ChatGPT and the release of GPT-4 in March 2023. The trend then dips in 2024 (3.2%) before surging to 14.2% in 2025 — the highest level in the dataset.

The 2024 dip is informative. It does not reflect a decline in AI capability; GPT-4o launched in May 2024, and Claude 3 became available in March 2024. Rather, it likely reflects a political lull: the Biden administration's final year produced fewer high-salience, contested rulemakings than the transition years of 2023 and 2025. This pattern is consistent with the adversarial mobilization hypothesis — AI adoption tracks political conflict, not technological availability.

A post-ChatGPT dummy variable (2023 and later) with agency fixed effects yields a coefficient of 0.065 (p < 0.001), indicating that the average AI score increased by 6.5 percentage points after ChatGPT's launch. A linear year trend with agency fixed effects produces a coefficient of 0.020 per year (p < 0.001). Both specifications control for agency-level heterogeneity and confirm that the temporal trend is not driven by any single agency.

The cross-domain simultaneity of the post-2022 surge — immigration, finance, health, and environment all rising together — is consistent with a supply-side technology shock interacting with pre-existing adversarial incentives. The technology became available to everyone in November 2022, but only commenters with adversarial incentives used it.

### F. The IRS-2023-0041 Anomaly: A Case Study in Coordinated AI Commenting

The full panel dataset reveals a dramatic outlier that merits separate discussion. Docket IRS-2023-0041, which received comments between October 2023 and January 2024, contains sixty-four scored comments with a mean AI score of 0.843 — by far the highest of any docket in the dataset. Fifty-three of the sixty-four comments (82.8%) score exactly 1.0, indicating near-certain AI generation. Only ten comments score 0.0.

This docket opened shortly after ChatGPT's launch and the release of GPT-4, during a period of intense public debate about cryptocurrency taxation and digital asset regulation. The LLM classification of these comments reveals a mix of stances: some advocate for blockchain-based solutions to banking inefficiencies, others argue for regulatory clarity on digital asset custody, and several make sophisticated arguments about the intersection of tax policy and financial innovation. The uniform AI detection scores — nearly all at the maximum — strongly suggest a coordinated campaign in which an organized interest group used AI to generate a large volume of individually varied comments on a financially significant tax rule.

The IRS-2023-0041 finding is significant for two reasons. First, it demonstrates that AI-generated comment campaigns are not limited to the politically charged immigration and environmental dockets that dominate the 2025 data. Financial industry stakeholders are also deploying AI to influence regulatory outcomes — and they were doing so within months of ChatGPT's release. Second, the docket's AI rate (84%) is so far above the dataset mean that it almost certainly reflects a single organized campaign rather than independent adoption by individual commenters. If a handful of such campaigns are removed from the data, the overall prevalence of AI-generated comments would be lower — but the concentration of AI use in adversarial, high-stakes contexts would be even more pronounced.

A similar pattern appears at the Office of the Comptroller of the Currency ("OCC"), where AI-generated comments increased from near-zero in 2019–2022 to 27% in 2025. The LLM classification of OCC AI-generated comments reveals distinctive content: arguments advocating for blockchain-based solutions ("RLUSD," "tokenized instruments"), calls for modernized digital asset custody regulations, and sophisticated arguments about bank-fintech partnership frameworks. These are not the concerns of ordinary citizens; they are the policy positions of the cryptocurrency and fintech industry, articulated with a polish and specificity that suggests organized professional advocacy.

### F. What Do AI-Generated Comments Look Like?

Qualitative review of high-scoring comments reveals three distinct patterns of AI use.

**Pattern 1: Mass-individualized advocacy.** Multiple comments share the same structural argument but with individually varied phrasing, vocabulary, and supporting points. None contain personal stories or identifying details. Example:

> "I strongly oppose the Interim Final Rule on Alien Registration... It reminds us of some of the worst moments in U.S. and world history when people were forced to register based on their race or nationality, leading to punishment and discrimination."[^31]

This pattern suggests advocacy organizations are using AI to generate *individualized* comment variations at scale — specifically to defeat agencies' practice of grouping and discounting identical form letters.

**Pattern 2: AI-structured policy arguments.** Comments using LLMs' characteristic header-then-explanation format to organize multiple policy objections:

> "Intrusion of Privacy: Reviewing someone's social media raises significant privacy concerns... Potential for Misuse: There is the risk that immigration officers may overstep boundaries... Contextual Misinterpretation: Social media posts can be taken out of context..."[^32]

**Pattern 3: AI as policy translator.** A smaller subset reflects genuine individual concern articulated through AI assistance:

> "I oppose the collection of social media identifiers due to significant security vulnerabilities... Bad actors could create fraudulent social media platforms specifically targeting potential immigrants."[^33]

This comment raises a specific, novel argument not found in advocacy talking points. It likely represents an individual who used AI to help articulate a genuine concern — a qualitatively different use case from Patterns 1 and 2, and one that raises distinct normative questions about when AI assistance enhances rather than undermines democratic participation.

---

## V. The Ideological Dimensions of AI-Generated Comments

### A. Regulatory Stance

To test whether AI-generated comments differ systematically in political content from human-written comments, I classify a subsample of 414 comments — all 138 scoring 1.0 and a stratified sample of 276 scoring 0.0 — on four dimensions using an automated LLM coder.

Regulatory stance does not differ significantly between AI and human comments. Among AI-generated comments, 58.0% support the proposed regulation and 40.6% oppose it. Among human comments, the split is 49.3% pro and 43.5% anti (χ² = 0.95, p = 0.33). AI is a tool used on both sides.

### B. Ideological Framing

Ideological framing, however, is significantly skewed. AI-generated comments are disproportionately coded as left-leaning: 74.6% left versus 17.4% right, compared to 60.5% left and 28.3% right among human comments (χ² = 6.40, p = 0.011; Fisher's exact OR = 1.93, p = 0.012).

This does not reflect bias in the AI models themselves. Rather, it reflects the political context of 2025: the organized mobilization campaigns that deployed AI at scale were predominantly left-coded — opposition to Trump administration immigration enforcement (USCIS, EOIR), defense of environmental protections (BLM, EPA, NOAA), and support for health and safety regulation (CMS, OSHA). Right-leaning commenters also use AI, but at lower rates and in fewer coordinated campaigns.

### C. The Amplification Pattern

The most legally significant finding is that AI amplifies the dominant position *within each docket*. AI comments do not uniformly favor one ideological direction. Instead, they intensify whichever position already predominates among the better-organized side of commenters. Table 3 illustrates this pattern across agencies with sufficient observations.

**Table 3: Regulatory Stance by Agency — AI vs. Human Comments**

| Agency | AI n | Human n | AI % Pro-Reg | Human % Pro-Reg | Pattern |
|--------|------|---------|-------------|----------------|---------|
| USCIS | 9 | 11 | 0% | 18% | Amplifies anti |
| EOIR | 3 | 13 | 0% | 23% | Amplifies anti |
| NOAA | 6 | 5 | 0% | 20% | Amplifies anti |
| ED | 7 | 14 | 14% | 57% | Reverses to anti |
| USDA | 16 | 32 | 31% | 56% | Amplifies anti |
| NHTSA | 10 | 20 | 100% | 50% | Reverses to pro |
| OSHA | 4 | 8 | 75% | 12% | Reverses to pro |
| BLM | 16 | 10 | 88% | 80% | Amplifies pro |
| OCC | 24 | 37 | 71% | 59% | Amplifies pro |
| CMS | 10 | 20 | 80% | 60% | Amplifies pro |
| IRS | 13 | 37 | 69% | 43% | Amplifies pro |

Three agencies exhibit outright *reversals*, where AI comments create a majority opposite to the human comment distribution:

At the **Department of Education**, 86% of AI comments oppose the proposed rule, compared to only 29% of human comments. The ED dockets in the 2025 data include Trump administration changes to student loan programs and school accountability standards, which attracted organized opposition from education advocacy groups and teachers' unions. The AI comments appear to originate from these campaigns, transforming what would appear to be a mixed human record into an apparently lopsided one opposing the rule.

At **NHTSA**, 100% of AI comments support the proposed vehicle safety regulation, compared to 50% of human comments. This is consistent with AI being deployed by consumer safety organizations to amplify support for regulations that industry commenters — car manufacturers and dealers — oppose in roughly equal measure.

At **OSHA**, the reversal is most dramatic: 75% of AI comments support workplace safety standards, while 87.5% of human comments oppose them. The human comment distribution at OSHA likely reflects regulated employers objecting to compliance costs — the traditional constituency for OSHA public comments. The AI comments likely originate from labor organizations and safety advocates who deploy AI to counter the employer voice. An agency reviewing its docket without AI detection would see a fundamentally different distribution of opinion than actually exists among human commenters.

This amplification pattern holds in nine of thirteen agencies with sufficient observations for comparison. It creates a paradox for agency decisionmakers: AI does not consistently favor one side, so agencies cannot apply a uniform correction. But AI *does* distort the apparent distribution of opinion on every docket where it is deployed, in whichever direction the better-organized side chooses. The distortion is not random noise — it is a systematic bias toward the preferences of whichever interests are most willing and able to deploy AI at scale.

The implications for administrative law are significant. Under current doctrine, agencies are not supposed to count votes — rulemaking is not a plebiscite.[^14] But in practice, agencies do attend to the volume and distribution of comment sentiment, particularly when facing political pressure or judicial review. An agency that receives 10,000 comments opposing a rule and 2,000 supporting it will take note of that ratio, even if it is not formally bound by it. If AI allows one side to inflate its apparent support from 2,000 to 10,000 comments — each individually authored, each raising slightly different points — the agency faces a distorted signal that may influence its decisionmaking in ways that are invisible to reviewing courts.

### D. Argument Quality

AI-generated comments score slightly but significantly higher on argument quality (mean 3.11 vs. 2.87 on a 1–5 scale, Mann-Whitney p = 0.027). They are more likely to be classified as "substantive-novel" (59% vs. 56%) but also more likely to be classified as "form letter" (20% vs. 15%). This bimodal quality distribution — AI producing both more polished arguments and more detectable boilerplate — corresponds to the two mechanisms of adversarial mobilization: organized campaigns generating form-letter variants, and individual citizens using AI to elevate their arguments.

The quality finding carries legal implications. Under the hard look doctrine, agencies must respond to *significant* comments — those raising novel factual, scientific, or legal points that bear on the agency's decision.[^34] If AI systematically increases the apparent quality of advocacy-group comments, agencies face a larger volume of ostensibly "significant" comments requiring response, straining administrative capacity and potentially delaying rulemaking. Consider the USCIS alien registration docket: the agency received over 5,400 comments, of which an estimated 23.6% were AI-generated. If each AI-generated comment raises a slightly different substantive argument — as the mass-individualization strategy is designed to ensure — the agency's legal obligation to respond to "significant" comments becomes dramatically more burdensome. The AI-generated comments are not form letters that can be grouped and dismissed; they are individually crafted arguments that, at least facially, demand individual consideration.

This dynamic creates a novel form of regulatory delay. Advocacy organizations have long used mass-comment campaigns to slow rulemaking by increasing agencies' processing burdens.[^52] AI supercharges this strategy: it allows a single organization to generate hundreds of individually varied, substantively detailed comments that each require agency attention, at a marginal cost approaching zero. The result is an asymmetric burden: the cost of generating AI comments is trivial, but the cost of responding to them under the hard look doctrine is substantial.

---

## VI. Toward a Legal Framework for AI-Generated Comments

### A. The Inadequacy of Existing Frameworks

Current legal frameworks for managing public comments are not designed for AI-generated text. The APA's procedural requirements are agnostic about the authorship of comments. Agencies' informal practices for handling mass comments depend on identifying textual duplication — a strategy that AI-individualized advocacy defeats by design. And the hard look doctrine, which requires agencies to engage with substantive arguments regardless of their provenance, creates perverse incentives for advocacy groups to use AI to manufacture "significant" comments that agencies are legally obligated to address.

The FCC's experience with its 2017 net neutrality proceeding is instructive.[^35] Millions of fraudulent comments were submitted using stolen identities, but the FCC processed them alongside legitimate submissions, and the D.C. Circuit in *Mozilla Corp. v. FCC* did not require the agency to have detected or excluded the fraudulent comments.[^36] If agencies are not required to police identity fraud, they are *a fortiori* not required to police AI-generated text — but the democratic legitimacy of the process depends on someone doing so.

### B. Disclosure Requirements

The most straightforward reform is a disclosure requirement. Congress or agencies could require commenters to disclose whether AI tools were used in drafting their comments, analogous to the disclosures required in securities filings[^37] or, more recently, in federal court filings.[^38] Several federal courts have already adopted standing orders requiring parties to disclose AI use in legal briefs.[^39]

A disclosure mandate could be implemented at the platform level. Regulations.gov could add a checkbox or dropdown menu requiring commenters to indicate whether their submission was drafted, edited, or generated with AI assistance. The Federal E-Rulemaking Initiative, which administers Regulations.gov, has the technical capacity to implement such a change without statutory amendment. The General Services Administration, which operates Regulations.gov, could implement this change through a platform update rather than a rulemaking — avoiding the ironic spectacle of a notice-and-comment proceeding on a rule about notice-and-comment.

The model here is the Lobbying Disclosure Act ("LDA"),[^53] which requires lobbyists to register and disclose their contacts with government officials. The LDA's disclosure regime is widely acknowledged to be imperfect — compliance is uneven, enforcement is rare, and the definition of covered activity is easily evaded.[^54] Yet the LDA has had meaningful effects on the culture of lobbying: it established a norm of transparency that shapes behavior even when enforcement is absent, and it created a public record that journalists, academics, and watchdog organizations use to monitor influence.[^55] An AI disclosure requirement for public comments could function similarly: imperfect in enforcement, but valuable in establishing a norm and creating a record.

**Counterarguments.** A disclosure requirement faces at least three objections. First, it is largely self-enforcing. Advocacy organizations deploying AI at scale have strong incentives not to disclose, and individual commenters may not understand when their use of AI tools (grammar correction, sentence rephrasing) rises to the level of "AI assistance." Second, a disclosure requirement might chill legitimate AI use — the "Pattern 3" translator use case described in Part IV — by stigmatizing any AI involvement in comment drafting. Third, mandating disclosure may raise First Amendment concerns, as the Supreme Court has recognized a right to anonymous speech that could extend to anonymous *assisted* speech.[^56]

These objections have force but are not dispositive. The self-enforcement problem is mitigated by the availability of independent AI detection tools: agencies can compare disclosed AI use rates against detected AI rates, and significant discrepancies can flag dockets for closer scrutiny. The chilling effect concern can be addressed through the design of the disclosure instrument — a graduated scale (e.g., "I drafted this myself," "I used AI for editing," "AI generated a draft that I reviewed") would normalize light AI assistance while flagging wholesale AI generation. And the First Amendment objection, while serious, is likely to fail under existing doctrine: compelled disclosure of the *method* of speech production is categorically different from compelled disclosure of the *identity* of the speaker, and the government's interest in the integrity of the regulatory process provides a sufficient justification under intermediate scrutiny.[^57]

### C. Detection-Assisted Processing

A more robust approach would integrate AI detection tools into agencies' comment-processing workflows. Under this model, agencies would run incoming comments through an AI detector — similar to the Pangram instrument used in this study — and flag comments with high AI scores for differential treatment.

This does not mean *discarding* AI-generated comments. The APA requires agencies to consider the substance of all relevant comments, regardless of authorship.[^40] But detection could enable agencies to *group* AI-generated comments that express the same underlying argument — much as they currently group identical form letters — and respond to the shared substance once rather than treating each AI-individualized variant as an independent viewpoint.

The validation study presented in Part II demonstrates that current detection technology is sufficiently reliable for this purpose. At 97.3% accuracy with zero false positives, the risk of incorrectly flagging genuine human comments is minimal. And because the purpose is grouping rather than exclusion, the consequences of a false positive — treating a human comment as part of a larger advocacy campaign — are modest compared to the alternative of treating thousands of AI-generated variants as independent expressions of individual opinion.

### D. Revised Judicial Review Standards

The hardest question is how courts should treat AI-generated comments on judicial review. The current hard look doctrine does not distinguish between arguments raised by individual citizens, advocacy organizations, or AI systems. A substantive point is a substantive point, regardless of who — or what — generated it.

I propose that courts adopt a modified standard that accounts for the provenance of comments in three ways.

First, courts should not find agency action arbitrary and capricious solely because the agency declined to respond individually to AI-generated comment variants that express the same underlying argument. Where an agency can demonstrate, using detection tools or other evidence, that a set of comments represents AI-individualized advocacy rather than independent citizen viewpoints, the agency should be permitted to group and respond to the shared substance — even if the comments' text is not literally identical. This is a natural extension of the *American Mining Congress* framework, which already permits agencies to group identical form letters.[^20] AI-individualized comments are functionally form letters — they express a single viewpoint through artificially varied language — and should be treated as such for purposes of the agency's obligation to respond.

Second, courts should give agencies latitude to develop expertise in AI detection and comment management. Just as courts defer to agency technical expertise on scientific and economic questions,[^41] they should defer to agency judgments about the provenance and representativeness of comments in their dockets, provided those judgments are explained and supported by the record. Post-*Loper Bright*, this deference is not *Chevron* deference to statutory interpretation, but rather the more general deference to agency factual and technical findings that survives the *Chevron* framework's demise.[^58] An agency's determination that a set of comments was generated by AI, based on validated detection tools and documented methodology, is a factual finding entitled to substantial evidence review — not de novo second-guessing by reviewing courts.

Third, courts should develop a clear standard for when AI provenance is relevant to the weight of a comment. I propose a distinction between *substantive relevance* and *representational relevance*. A comment's substantive content — the factual claims it makes, the legal arguments it raises, the data it cites — is relevant regardless of its provenance. An AI-generated comment that identifies a genuine flaw in an agency's cost-benefit analysis must be addressed on the merits, just as a ghostwritten comment from a law firm must be. But a comment's *representational* weight — its value as evidence that real people hold a particular view and will be affected by the rule in a particular way — is diminished when the comment is AI-generated. An agency that gives less representational weight to AI-generated comments is not making a judgment about the merits of the argument; it is making a judgment about the evidentiary value of the comment as an indicator of public sentiment. This distinction is consistent with the APA's structure: agencies must consider the *substance* of comments, but they have discretion in weighing the *representativeness* of the record.

**Counterarguments.** The principal objection to modified judicial review standards is that they empower agencies to discount comments from disfavored groups. If agencies can label comments as "AI-generated" and give them less weight, what prevents an agency from selectively applying detection tools to discount opposing comments while crediting supportive ones? This concern is real, and it underscores the importance of transparency: any agency that applies AI detection in its comment-processing workflow should be required to disclose its methodology, apply it uniformly across all comments in a docket, and include the detection results in the administrative record available for judicial review. The transparency requirement converts what might otherwise be an invitation to bias into an auditable, challengeable procedure.

### E. The Democratization Counterargument

Not all AI use in public comments is normatively problematic. Pattern 3, identified in Part IV — the individual citizen using AI to articulate a genuine concern they could not have expressed on their own — represents a potentially *democratizing* use of the technology. If AI helps less educated or less politically sophisticated citizens participate meaningfully in rulemaking, it serves the APA's purpose of broad public engagement.[^42]

Any legal framework for AI-generated comments must distinguish between AI as a *translator* of genuine human preferences and AI as a *manufacturer* of artificial advocacy. The disclosure and detection approaches proposed above can help agencies make this distinction: a single AI-assisted comment from an individual is qualitatively different from thousands of AI-individualized comments from a coordinated campaign. The former enhances democratic participation; the latter undermines it.

---

### F. Looking Forward: AI Watermarking and Technical Solutions

The proposals above — disclosure, detection, and judicial review reform — are designed for the current technological moment, in which AI detection is reliable but imperfect and AI watermarking is nascent. As the technology evolves, more robust technical solutions may become available.

Several AI developers, including OpenAI, Google DeepMind, and Anthropic, have explored embedding invisible watermarks in AI-generated text — statistical signatures that allow generated text to be identified with high confidence even after minor editing.[^59] The Biden administration's October 2023 Executive Order on AI Safety included commitments from leading AI companies to develop watermarking standards.[^60] If effective watermarking were widely deployed, agencies could identify AI-generated comments with near-perfect accuracy, rendering the detection challenges discussed in Part II largely moot.

But watermarking faces a fundamental limitation: it requires the cooperation of the AI provider. Open-source models, which anyone can run without watermarking, are already widely available, and their capabilities are rapidly approaching those of commercial models. A determined advocacy organization could generate AI comments using an open-source model that produces no watermark, defeating any watermark-based detection scheme. Watermarking is therefore best understood as a complement to, rather than a replacement for, the detection-assisted processing framework proposed above.

A more promising long-term approach may be to shift the question from "was this comment AI-generated?" to "does this comment represent an independent viewpoint?" Advances in natural language processing and semantic clustering could enable agencies to identify groups of comments that express the same underlying argument — regardless of whether they were written by humans or machines — and treat them as a single viewpoint for purposes of response. This approach would sidestep the AI detection problem entirely by focusing on the substantive redundancy of comments rather than their provenance. It would also address a pre-AI problem: human-organized letter-writing campaigns that produce varied but substantively identical comments already pose the same representational challenge that AI amplifies.

---

## VII. Limitations

Several limitations constrain interpretation of these results, and candor about them is important for a study making strong claims about a novel phenomenon.

**Detection accuracy.** While the validation study demonstrates 97.3% accuracy with zero false positives, the validation set is small (n = 75) and covers only two AI model families (Claude and GPT-5). Pangram's accuracy on text from other models (Gemini, Llama, Mistral) or on AI-assisted text — where a human writes a draft and uses AI for editing — is unknown. The bimodal distribution of scores in the wild data (mass at 0.0 and mass at 1.0) suggests that most AI use in the dataset is wholesale generation rather than light editing, but AI-assisted comments in the middle of the distribution may be undercounted.

**Sample size.** The cross-sectional dataset contains 498 comments across sixteen agencies. Several agency-level estimates rest on small samples: FHWA (n = 10), OCC (n = 3), USDA (n = 7). The full panel dataset (5,326 comments) provides more robust estimates, but individual agency-year cells may still be noisy. The IRS-2023-0041 finding (84% AI) is based on sixty-four comments and is almost certainly driven by a single organized campaign; generalizing from one docket to an agency-wide pattern is inappropriate.

**Causal identification.** The adversarial mobilization hypothesis is supported by strong correlational patterns — the NPS-BLM comparison, the IRS-2023 anomaly, the post-ChatGPT inflection — but the study design is observational. I cannot rule out the possibility that omitted variables (commenter demographics, docket complexity, agency-specific commenting cultures) explain some of the variation attributed to political salience. The NPS-BLM comparison is the strongest quasi-experimental evidence in the data, but even it relies on the assumption that the commenter populations are comparable — an assumption that cannot be directly tested without individual-level demographic data that Regulations.gov does not collect.

**LLM classification.** The ideological and stance classifications in Part V rely on Claude Haiku as an automated coder. While LLM-based classification has been validated in political science contexts and produces reliable results on clear cases,[^61] it introduces a layer of measurement uncertainty that hand-coding would avoid. The classifications should be treated as indicators of broad patterns rather than precise measurements of individual comments.

**Temporal coverage.** The 2024 dip in AI scores may reflect genuine political dynamics (fewer high-salience rulemakings in Biden's final year) or sampling artifacts (the 2024 data may underrepresent high-conflict dockets that were active but whose comments had not yet been posted to Regulations.gov at the time of data collection). The temporal trend should be replicated with more complete 2024 coverage before drawing strong conclusions about year-over-year dynamics.

Despite these limitations, the core findings — that AI-generated content is present in a substantial share of 2025 public comments, that adoption varies dramatically by regulatory context, and that the variation is consistent with adversarial mobilization rather than technological diffusion — are robust across multiple specifications and datasets.

---

## Conclusion

The notice-and-comment process was designed for a world in which writing was costly and comments were scarce. The process survived its first technological disruption — the migration from paper letters to electronic submissions via Regulations.gov — because the fundamental relationship between commenter effort and comment production remained intact. Writing a comment still required a human to formulate thoughts, compose sentences, and express a view. AI severs this link. For the first time in the eighty-year history of notice-and-comment rulemaking, the marginal cost of producing a substantive, individually authored public comment is approaching zero.

The data presented in this Article establish four facts. First, AI-generated content is already prevalent in federal public comments, present in nearly one in five submissions in 2025, with some dockets exceeding 80%. Second, adoption is concentrated in adversarial regulatory contexts, driven by political mobilization and industry stakeholder campaigns rather than gradual technological diffusion. Third, AI-generated comments are ideologically asymmetric in the current political moment, disproportionately amplifying left-coded mobilization campaigns against Trump administration rulemakings while reinforcing the dominant position within each docket. Fourth, AI-generated comments systematically distort the apparent distribution of public opinion in ways that are invisible to agencies using current processing methods — and that are particularly insidious because they vary by docket rather than uniformly favoring one ideological direction.

These facts demand a legal response, but the response must be calibrated. Not all AI use in public comments is harmful. The individual citizen who uses AI to translate genuine concern into polished prose is exercising democratic agency, not undermining it. The advocacy organization that uses AI to help non-English speakers participate in rulemakings that affect their lives is expanding the reach of the notice-and-comment process. The normative challenge is distinguishing these *democratizing* uses from the *manufacturing* uses — the coordinated campaigns that exploit AI to inflate the apparent breadth and quality of advocacy on behalf of narrow interests.

The proposals outlined in Part VI — disclosure requirements, detection-assisted processing, and modified judicial review standards — are designed to make this distinction operationally feasible. They do not require the APA to be amended, though statutory reform would strengthen the framework. They do not require agencies to ignore AI-generated comments, only to process them with awareness of their provenance. And they preserve the possibility that AI can enhance democratic participation while limiting its use as a tool of manufactured consent.

The alternative — processing AI-generated comments as if they were authentic expressions of individual human judgment — is not neutrality. It is a choice to allow the notice-and-comment process to be captured by whichever interests are most willing and able to deploy AI at scale. The IRS-2023-0041 docket, in which 83% of comments were AI-generated within months of ChatGPT's release, is not an aberration. It is a preview. As AI tools become more capable and more widely adopted, the question is not whether AI will transform the notice-and-comment process, but whether the legal framework will adapt quickly enough to preserve its democratic legitimacy.

The APA was written for a world of paper and typewriters. It has proven remarkably durable — adaptable enough to accommodate electronic filing, mass email campaigns, and comment volumes in the millions. Whether it can accommodate artificial intelligence depends on whether agencies, courts, and Congress are willing to confront the uncomfortable truth that the notice-and-comment process's most fundamental assumption — that comments are written by people — is no longer reliable.

---

## References

[^1]: Kenneth Culp Davis, *Administrative Law Treatise* § 6.15 (1958).
[^2]: 5 U.S.C. § 553 (2018).
[^3]: *Id.* § 553(c).
[^4]: *See, e.g.*, *Portland Cement Ass'n v. Ruckelshaus*, 486 F.2d 375, 393–94 (D.C. Cir. 1973).
[^5]: Motor Vehicle Mfrs. Ass'n v. State Farm Mut. Auto. Ins. Co., 463 U.S. 29, 43 (1983).
[^6]: *See* Tom B. Brown et al., *Language Models Are Few-Shot Learners*, 33 Advances in Neural Info. Processing Sys. 1877 (2020); OpenAI, *GPT-4 Technical Report* (2023).
[^7]: *See* Cary Coglianese, *Citizen Participation in Rulemaking: Past, Present, and Future*, 55 Duke L.J. 943, 968 (2006).
[^8]: 5 U.S.C. § 553(c).
[^9]: *Id.*
[^10]: *Id.*
[^11]: *State Farm*, 463 U.S. at 43.
[^12]: *See* *Pub. Citizen v. Steed*, 733 F.2d 93, 101 (D.C. Cir. 1984).
[^13]: United States v. Nova Scotia Food Prods. Corp., 568 F.2d 240, 252 (2d Cir. 1977).
[^14]: *See* Coglianese, *supra* note 7, at 968.
[^15]: Action on Smoking & Health v. CAB, 699 F.2d 1209, 1216 (D.C. Cir. 1983).
[^16]: *See* *Home Box Office, Inc. v. FCC*, 567 F.2d 9, 35–36 (D.C. Cir. 1977).
[^17]: Cary Coglianese, *E-Rulemaking: Information Technology and the Regulatory Process*, 56 Admin. L. Rev. 353, 380 (2004).
[^18]: *See* N.Y. Att'y Gen., *Fake Comments: How U.S. Companies & Partisans Hack Democracy* (2021).
[^19]: *See* Administrative Conference of the United States, Recommendation 2021-1, *Managing Mass, Computer-Generated, and Fraudulent Comments* (2021).
[^20]: *Am. Mining Cong. v. EPA*, 965 F.2d 759, 771 (9th Cir. 1992).
[^21]: Greater Boston Television Corp. v. FCC, 444 F.2d 841, 851 (D.C. Cir. 1970).
[^22]: *State Farm*, 463 U.S. at 43.
[^23]: Pangram Labs, *Pangram AI Detection API v3* (2025), https://text.api.pangram.com.
[^24]: *See* Vinu Sankar Sadasivan et al., *Can AI-Generated Text Be Reliably Detected?* (2023).
[^25]: *See* Matthew Dahl et al., *Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models*, J. Legal Analysis (2024).
[^26]: *See* Eric Mitchell et al., *DetectGPT: Zero-Shot Machine-Generated Text Detection Using Probability Curvature*, Proceedings of the 40th Int'l Conf. on Machine Learning (2023).
[^27]: Full-range page sampling probes the total comment count for each agency-year, then draws random pages across the entire accessible range — not just the first pages — ensuring that comments from low-volume and high-volume dockets are represented in proportion to their share of the comment stream.
[^28]: Anthropic, *Claude 3.5 Haiku Model Card* (2025).
[^29]: *See* Sunita Desai & J. Michael McWilliams, *Consequences of the 340B Drug Pricing Program*, 378 New Eng. J. Med. 539 (2018).
[^30]: *See* Nick Decker, *Who Uses AI in Congress?* (Working Paper, 2026).
[^31]: USCIS-2025-0004-3769, 160 words, Pangram AI score: 1.0.
[^32]: USCIS-2025-0003-0279, 332 words, Pangram AI score: 1.0.
[^33]: USCIS-2025-0003-0174, 167 words, Pangram AI score: 1.0.
[^34]: *See* *Portland Cement*, 486 F.2d at 393–94.
[^35]: *See* N.Y. Att'y Gen., *supra* note 18.
[^36]: *Mozilla Corp. v. FCC*, 940 F.3d 1, 64–65 (D.C. Cir. 2019).
[^37]: *See, e.g.*, 17 C.F.R. § 229.601 (requiring disclosure of material contracts).
[^38]: *See, e.g.*, Standing Order, *In re Use of Artificial Intelligence*, No. 23-mc-3223 (N.D. Tex. May 30, 2023) (Starr, J.).
[^39]: *See, e.g.*, *id.*; Standing Order, *Artificial Intelligence*, No. 23-mc-1 (E.D. Pa. June 6, 2023).
[^40]: 5 U.S.C. § 553(c).
[^41]: *See* *Chevron U.S.A., Inc. v. NRDC*, 467 U.S. 837, 865 (1984) (deferring to agency expertise); *but see* *Loper Bright Enters. v. Raimondo*, 144 S. Ct. 2244 (2024) (overruling *Chevron* deference).
[^42]: *See* Beth Simone Noveck, *The Electronic Revolution in Rulemaking*, 53 Emory L.J. 433, 440 (2004).
[^43]: Nina A. Mendelson, *Rulemaking, Democracy, and Torrents of E-Mail*, 79 Geo. Wash. L. Rev. 1343, 1351–55 (2011).
[^44]: Coglianese, *supra* note 7, at 958–62.
[^45]: Michael A. Livermore & Richard L. Revesz, *Can Machine Learning Aid in Regulatory Analysis?*, 53 Conn. L. Rev. 1 (2021).
[^46]: Perez v. Mortgage Bankers Ass'n, 575 U.S. 92, 96 (2015).
[^47]: Administrative Conference of the United States, Recommendation 2021-1, *Managing Mass, Computer-Generated, and Fraudulent Comments* (June 17, 2021).
[^48]: *Id.* ¶¶ 3–5.
[^49]: N.Y. Att'y Gen., *Fake Comments: How U.S. Companies & Partisans Hack Democracy* 7–12 (2021).
[^50]: *Mozilla Corp. v. FCC*, 940 F.3d 1, 64–65 (D.C. Cir. 2019).
[^51]: Stuart Minor Benjamin, *Algorithms and Speech*, 161 U. Pa. L. Rev. 1445, 1480–85 (2013).
[^52]: *See* Wendy E. Wagner, *Administrative Law, Filter Failure, and Legitimacy*, 59 Duke L.J. 1321, 1345 (2010) (describing the use of mass comments as a strategy to increase agency processing costs and delay rulemaking).
[^53]: Lobbying Disclosure Act of 1995, 2 U.S.C. §§ 1601–1614.
[^54]: *See* Lee Drutman, *The Business of America Is Lobbying* 89–95 (2015).
[^55]: *Id.* at 96–100.
[^56]: *See* McIntyre v. Ohio Elections Comm'n, 514 U.S. 334, 341–42 (1995) (recognizing First Amendment protection for anonymous political speech).
[^57]: *Cf.* *Citizens United v. FEC*, 558 U.S. 310, 366–71 (2010) (upholding disclosure requirements for political speech under a less demanding standard than the expenditure limits struck down in the same case).
[^58]: *See* *Loper Bright Enters. v. Raimondo*, 144 S. Ct. 2244, 2273 (2024) (overruling *Chevron* deference while preserving deference to agency factual determinations under the substantial evidence standard).
[^59]: *See* John Kirchenbauer et al., *A Watermark for Large Language Models*, Proceedings of the 40th Int'l Conf. on Machine Learning (2023).
[^60]: Exec. Order No. 14,110, 88 Fed. Reg. 75,191 (Oct. 30, 2023).
[^61]: *See* Andrew Eggers et al., *No, Large Language Models Cannot Reliably Rate Arguments in Political Science*, Pol. Analysis (2025) (discussing validation challenges while acknowledging LLM reliability for clear classification tasks).

---

*Data and replication code available at: https://github.com/stevie-ml/ai-public-comments*
