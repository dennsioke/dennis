# Rubrics - Retail Shelf Object Detection

## Rubric 1: Baseline Detection
**Points:** 25
**Criteria:** mAP@0.50 >= 0.30 on the private test set across all 10 product categories.

## Rubric 2: Competitive Detection
**Points:** 30
**Criteria:** mAP@0.50 >= 0.45. Handles occluded and truncated objects with per-class AP >= 0.25 on at least 7 categories.

## Rubric 3: High-Quality Detection
**Points:** 25
**Criteria:** mAP@0.50 >= 0.60. Demonstrates effective use of anchor-based or anchor-free detection architecture.

## Rubric 4: Expert Detection
**Points:** 20
**Criteria:** mAP@0.50 >= 0.72. Near-production quality with strong performance on the most crowded shelf sections.

## Scoring Notes

- Predictions CSV must have columns: `image_id`, `category`, `bbox_x`, `bbox_y`, `bbox_w`, `bbox_h`, `score`
- Bounding box coordinates are normalized [0,1] in [x, y, w, h] format
- IoU threshold for matching: 0.50
- Missing images receive AP = 0 for all their ground truth objects
- Total possible score: 100 points
