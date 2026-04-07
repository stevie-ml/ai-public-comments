## 03_analysis.R
## Figures and regression tables for "Who Uses AI to Comment on Federal Rules?"
##
## Usage: Rscript scripts/03_analysis.R

library(tidyverse)
library(lmtest)
library(sandwich)
library(stargazer)

DATA_CROSS <- "data/comments_merged.csv"
DATA_TS    <- "data/comments_timeseries.csv"
OUT        <- "paper/figures/"
TAB_OUT    <- "paper/tables/"

# ── Cross-Sectional Analysis ─────────────────────────────────────────────────

df <- read_csv(DATA_CROSS) %>%
  filter(!is.na(ai_score)) %>%
  mutate(
    ai_binary = as.integer(ai_score > 0.1),
    log_wc    = log(word_count),
    category  = factor(category, levels = c(
      "agriculture", "public_lands_routine", "labor",
      "finance", "health",
      "political_immigration", "political_environment"
    )),
    agency = factor(agency)
  )

cat(sprintf("N = %d comments, %d agencies\n", nrow(df), n_distinct(df$agency)))

# Color scheme
cat_colors <- c(
  "political_environment"  = "#C0392B",
  "political_immigration"  = "#E74C3C",
  "health"                 = "#D35400",
  "finance"                = "#2980B9",
  "labor"                  = "#27AE60",
  "public_lands_routine"   = "#8E44AD",
  "agriculture"            = "#7F8C8D"
)

cat_labels <- c(
  "political_environment"  = "Political / Environment",
  "political_immigration"  = "Political / Immigration",
  "health"                 = "Health Policy",
  "finance"                = "Finance & Compliance",
  "labor"                  = "Labor",
  "public_lands_routine"   = "Public Lands (routine)",
  "agriculture"            = "Agriculture"
)

# ── Figure 1: Mean AI Score by Agency ─────────────────────────────────────────

agency_summary <- df %>%
  group_by(agency, category) %>%
  summarise(
    n = n(), mean_ai = mean(ai_score),
    se_ai = sd(ai_score) / sqrt(n()),
    .groups = "drop"
  ) %>%
  mutate(agency = fct_reorder(agency, mean_ai))

p1 <- ggplot(agency_summary, aes(x = agency, y = mean_ai, fill = category)) +
  geom_col(width = 0.7, alpha = 0.9) +
  geom_errorbar(aes(ymin = mean_ai - 1.96 * se_ai,
                    ymax = mean_ai + 1.96 * se_ai),
                width = 0.25, color = "gray30") +
  geom_text(aes(label = sprintf("n=%d", n)),
            hjust = -0.15, size = 3, color = "gray40") +
  scale_fill_manual(values = cat_colors, labels = cat_labels,
                    name = "Regulatory context") +
  scale_y_continuous(labels = scales::percent_format(accuracy = 1),
                     limits = c(0, 0.55)) +
  coord_flip() +
  labs(
    title = "AI Adoption Varies Sharply by Regulatory Context",
    subtitle = "Mean AI content score (Pangram v3) by federal agency, 2025",
    x = NULL, y = "Mean AI score",
    caption = "Error bars = 95% CI. N = 498 comments across 16 agencies."
  ) +
  theme_minimal(base_size = 12) +
  theme(legend.position = "bottom", plot.title = element_text(face = "bold"),
        panel.grid.major.y = element_blank(), panel.grid.minor = element_blank())

ggsave(paste0(OUT, "fig1_agency_ai.pdf"), p1, width = 8, height = 5)
ggsave(paste0(OUT, "fig1_agency_ai.png"), p1, width = 8, height = 5, dpi = 200)

# ── Figure 2: Word Count ─────────────────────────────────────────────────────

df_wc <- df %>%
  mutate(ai_group = case_when(
    ai_score == 0   ~ "Human (score = 0)",
    ai_score < 0.5  ~ "Mixed (0 < score < 0.5)",
    TRUE            ~ "AI (score >= 0.5)"
  ) %>% factor(levels = c("Human (score = 0)", "Mixed (0 < score < 0.5)", "AI (score >= 0.5)")))

p2 <- ggplot(df_wc, aes(x = word_count, fill = ai_group)) +
  geom_histogram(bins = 35, alpha = 0.75, position = "identity") +
  scale_fill_manual(values = c("#2ECC71", "#F39C12", "#E74C3C")) +
  scale_x_continuous(limits = c(0, 900)) +
  facet_wrap(~ai_group, ncol = 1, scales = "free_y") +
  labs(title = "AI-Generated Comments Are Longer",
       x = "Word count", y = "Count") +
  theme_minimal(base_size = 12) +
  theme(legend.position = "none", plot.title = element_text(face = "bold"))

ggsave(paste0(OUT, "fig2_wordcount.pdf"), p2, width = 7, height = 5)
ggsave(paste0(OUT, "fig2_wordcount.png"), p2, width = 7, height = 5, dpi = 200)

# ── Regression Table 1 ───────────────────────────────────────────────────────

m1 <- lm(ai_score ~ category, data = df)
m2 <- lm(ai_score ~ category + log_wc, data = df)
m3 <- lm(ai_score ~ agency + log_wc, data = df)

se1 <- sqrt(diag(vcovHC(m1, type = "HC3")))
se2 <- sqrt(diag(vcovHC(m2, type = "HC3")))
se3 <- sqrt(diag(vcovHC(m3, type = "HC3")))

stargazer(m1, m2, m3,
  se = list(se1, se2, se3),
  title = "Determinants of AI Content in Federal Public Comments",
  dep.var.labels = "AI score (Pangram v3)",
  omit = "^agency",
  add.lines = list(c("Agency FE", "No", "No", "Yes"),
                   c("Category FE", "Yes", "Yes", "No")),
  omit.stat = c("f", "ser"),
  notes = "HC3 robust standard errors. Reference: Agriculture.",
  out = paste0(TAB_OUT, "table1_regression.tex"),
  type = "latex"
)

# ── Figure 3: Time Series ────────────────────────────────────────────────────

if (file.exists(DATA_TS)) {
  ts_raw <- read_csv(DATA_TS, show_col_types = FALSE) %>%
    filter(!is.na(ai_score))

  agency_cats <- ts_raw %>% distinct(agency, category)
  agency_colors <- setNames(cat_colors[agency_cats$category], agency_cats$agency)

  ts_df <- ts_raw %>%
    group_by(year, agency, category) %>%
    summarise(n = n(), mean_ai = mean(ai_score),
              se_ai = sd(ai_score) / sqrt(n()), .groups = "drop") %>%
    filter(n >= 10)

  p3 <- ggplot(ts_df, aes(x = year, y = mean_ai, color = agency, group = agency)) +
    geom_ribbon(aes(ymin = pmax(0, mean_ai - 1.96 * se_ai),
                    ymax = mean_ai + 1.96 * se_ai, fill = agency),
                alpha = 0.12, color = NA) +
    geom_line(linewidth = 0.9) +
    geom_point(aes(size = n), alpha = 0.9) +
    geom_vline(xintercept = 2022 + 10/12, linetype = "dashed", color = "gray50") +
    annotate("text", x = 2022 + 10/12 + 0.08, y = 0.32,
             label = "ChatGPT\nlaunched", hjust = 0, size = 2.8, color = "gray40") +
    scale_color_manual(values = agency_colors) +
    scale_fill_manual(values = agency_colors) +
    scale_size_continuous(range = c(2, 6), guide = "none") +
    scale_x_continuous(breaks = 2019:2025) +
    scale_y_continuous(labels = scales::percent_format(accuracy = 1), limits = c(0, NA)) +
    labs(title = "AI Adoption in Public Comments Has Risen Since 2022",
         subtitle = "Mean Pangram AI score by agency and year (2019-2025)",
         x = NULL, y = "Mean AI score") +
    theme_minimal(base_size = 12) +
    theme(legend.position = "none", plot.title = element_text(face = "bold"))

  ggsave(paste0(OUT, "fig3_timeseries.pdf"), p3, width = 9, height = 5)
  ggsave(paste0(OUT, "fig3_timeseries.png"), p3, width = 9, height = 5, dpi = 200)

  # Time-series regressions
  ts_reg <- ts_raw %>%
    mutate(post_chatgpt = as.integer(year >= 2023),
           year_c = year - 2019, agency = factor(agency),
           log_wc = log(word_count))

  m_t1 <- lm(ai_score ~ year_c, data = ts_reg)
  m_t2 <- lm(ai_score ~ year_c + agency, data = ts_reg)
  m_t3 <- lm(ai_score ~ year_c + agency + log_wc, data = ts_reg)
  m_t4 <- lm(ai_score ~ post_chatgpt + agency, data = ts_reg)

  se_t1 <- sqrt(diag(vcovHC(m_t1, type = "HC3")))
  se_t2 <- sqrt(diag(vcovHC(m_t2, type = "HC3")))
  se_t3 <- sqrt(diag(vcovHC(m_t3, type = "HC3")))
  se_t4 <- sqrt(diag(vcovHC(m_t4, type = "HC3")))

  stargazer(m_t1, m_t2, m_t3, m_t4,
    se = list(se_t1, se_t2, se_t3, se_t4),
    title = "Time Trends in AI Content of Federal Public Comments",
    dep.var.labels = "AI score (Pangram v3)",
    covariate.labels = c("Year (0 = 2019)", "Post-ChatGPT (2023+)", "Log(word count)"),
    omit = "^agency",
    add.lines = list(c("Agency FE", "No", "Yes", "Yes", "Yes")),
    omit.stat = c("f", "ser"),
    out = paste0(TAB_OUT, "table2_timeseries.tex"),
    type = "latex"
  )
}

cat("Done.\n")
