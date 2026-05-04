# Rubrics - News Article Seq2Seq Summarization

## Rubric 1: Baseline Summarization
**Points:** 25
**Criteria:** Average ROUGE-L F1 >= 0.25 across all test articles. Must generate text (not extract sentences verbatim).

## Rubric 2: Competitive Summarization
**Points:** 30
**Criteria:** Average ROUGE-L F1 >= 0.35. ROUGE-1 >= 0.40 and ROUGE-2 >= 0.15.

## Rubric 3: High-Quality Summarization
**Points:** 25
**Criteria:** Average ROUGE-L F1 >= 0.42. Summaries are abstractive (not extractive) with less than 30% exact n-gram overlap with article.

## Rubric 4: State-of-the-Art Summarization
**Points:** 20
**Criteria:** Average ROUGE-L F1 >= 0.48. Consistent performance across all five topic domains (per-domain ROUGE-L >= 0.40).

## Scoring Notes

- Predictions CSV must have columns: `article_id`, `predicted_summary`
- ROUGE scores are computed using standard tokenization (lowercase, no stemming)
- Summary length is not penalized but empty predictions receive ROUGE = 0
- Total possible score: 100 points
