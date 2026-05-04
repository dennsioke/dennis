# Plant Disease Detection Computer Vision Dataset

## Overview

This dataset contains synthetic metadata representing plant leaf images labeled with disease categories across five crop types. Images are described by extracted features suitable for computer vision model training and evaluation.

## Dataset Details

- **Title:** Agriculture Plant Leaf Disease Detection Computer Vision Dataset
- **License:** CC0 Public Domain
- **Source:** Synthetic
- **Format:** CSV (feature-based) + image metadata
- **Size:** ~25,000 records

## Schema

| Column | Type | Description |
|--------|------|-------------|
| image_id | int | Unique image identifier |
| crop_type | string | Type of crop (tomato, potato, corn, wheat, grape) |
| disease | string | Disease label (see classes below) |
| severity | string | mild, moderate, severe |
| leaf_color_r | float | Mean red channel value (0-255) |
| leaf_color_g | float | Mean green channel value (0-255) |
| leaf_color_b | float | Mean blue channel value (0-255) |
| texture_contrast | float | Local binary pattern contrast |
| texture_homogeneity | float | GLCM texture homogeneity |
| lesion_area_pct | float | Percentage of leaf area with lesions |
| image_width | int | Image width in pixels |
| image_height | int | Image height in pixels |
| brightness | float | Mean image brightness |

## Disease Classes (11 classes)

| Class | Crop |
|-------|------|
| healthy | all |
| early_blight | tomato, potato |
| late_blight | tomato, potato |
| leaf_mold | tomato |
| powdery_mildew | corn, wheat, grape |
| gray_leaf_spot | corn |
| rust | wheat, corn |
| black_rot | grape |
| downy_mildew | grape |
| septoria | wheat |
| mosaic_virus | tomato |

## Usage

Train and evaluate a computer vision classification model. The feature columns simulate image-derived representations. Participants may use these directly or simulate image patch extraction. Evaluation is macro-averaged F1.
