# Rubrics - NLP Tweet Sentiment Classification

## Rubric 1: Baseline Classification Performance
**Points:** 30
**Criteria:** Macro-averaged F1 score >= 0.60 on the private test set across all five sentiment classes.

## Rubric 2: Competitive Performance
**Points:** 40
**Criteria:** Macro-averaged F1 score >= 0.72 on the private test set. Demonstrates meaningful use of text features or pre-trained representations.

## Rubric 3: Top-Tier Performance
**Points:** 30
**Criteria:** Macro-averaged F1 score >= 0.78 on the private test set. Model handles class imbalance and edge cases effectively.

## Scoring Notes

- Predictions must be a CSV with columns: `tweet_id`, `predicted_sentiment`
- Labels must exactly match: `positive`, `negative`, `neutral`, `angry`, `sad`
- Missing predictions receive a score of 0 for those samples
- External datasets are not permitted
- Total possible score: 100 points
