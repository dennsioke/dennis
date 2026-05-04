# Rubrics - Plant Disease Detection

## Rubric 1: Baseline Detection
**Points:** 25
**Criteria:** Macro-averaged F1 >= 0.55 across all 11 disease classes.

## Rubric 2: Multi-Crop Generalization
**Points:** 30
**Criteria:** Macro-averaged F1 >= 0.65. Model must achieve F1 >= 0.50 on at least 4 different crop types individually.

## Rubric 3: High Accuracy Detection
**Points:** 25
**Criteria:** Macro-averaged F1 >= 0.75. Effective use of crop-type context and texture features.

## Rubric 4: Expert-Level Performance
**Points:** 20
**Criteria:** Macro-averaged F1 >= 0.82. Near-human performance on the hardest disease classes (rust, mosaic_virus, late_blight).

## Scoring Notes

- Predictions CSV must have columns: `image_id`, `predicted_disease`
- All 11 labels must be representable in predictions: `healthy`, `early_blight`, `late_blight`, `leaf_mold`, `powdery_mildew`, `gray_leaf_spot`, `rust`, `black_rot`, `downy_mildew`, `septoria`, `mosaic_virus`
- External datasets not permitted
- Total possible score: 100 points
