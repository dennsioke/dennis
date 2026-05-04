# Rubrics - Medical Text BERT Fine-Tuning Classification

## Rubric 1: Baseline Fine-Tuning
**Points:** 25
**Criteria:** Macro-averaged F1 score >= 0.65 on the private test set. Model must be a fine-tuned transformer, not a bag-of-words baseline.

## Rubric 2: Domain-Adapted Performance
**Points:** 35
**Criteria:** Macro-averaged F1 score >= 0.75. Evidence of domain-specific adaptation (e.g., BioBERT, ClinicalBERT weights or custom tokenization).

## Rubric 3: High-Quality Fine-Tuning
**Points:** 25
**Criteria:** Macro-averaged F1 score >= 0.82. Effective handling of class imbalance and medical abbreviations.

## Rubric 4: State-of-the-Art Approach
**Points:** 15
**Criteria:** Macro-averaged F1 score >= 0.87. Demonstrates advanced fine-tuning techniques (e.g., layer-wise learning rate decay, data augmentation).

## Scoring Notes

- Predictions CSV must have columns: `note_id`, `predicted_condition`
- Labels must exactly match: `cardiovascular`, `respiratory`, `neurological`, `gastrointestinal`, `musculoskeletal`, `endocrine`, `dermatological`
- External medical datasets are not allowed
- Total possible score: 100 points
