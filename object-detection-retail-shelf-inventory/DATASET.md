# Retail Shelf Object Detection Dataset

## Overview

This synthetic dataset simulates object detection annotations for retail shelf items. It contains bounding box annotations for products on store shelves — modeling a real-world retail inventory management use case.

## Dataset Details

- **Title:** Retail Industry Shelf Product Object Detection Dataset
- **License:** CC0 Public Domain
- **Source:** Synthetic
- **Format:** CSV (COCO-style annotations)
- **Size:** 10,000 images, ~80,000 bounding box annotations

## Files

| File | Description |
|------|-------------|
| images.csv | Image metadata |
| annotations.csv | Bounding box annotations |

## Images Schema

| Column | Type | Description |
|--------|------|-------------|
| image_id | int | Unique image identifier |
| filename | string | Simulated filename |
| width | int | Image width px |
| height | int | Image height px |
| shelf_section | string | Store section: grocery, beverages, snacks, dairy, household |
| num_objects | int | Total annotated objects in image |

## Annotations Schema

| Column | Type | Description |
|--------|------|-------------|
| annotation_id | int | Unique annotation ID |
| image_id | int | Reference to image |
| category | string | Product category label |
| bbox_x | float | Top-left x coordinate (normalized 0-1) |
| bbox_y | float | Top-left y coordinate (normalized 0-1) |
| bbox_w | float | Bounding box width (normalized 0-1) |
| bbox_h | float | Bounding box height (normalized 0-1) |
| confidence_gt | float | Ground truth annotation confidence |
| occluded | bool | Whether object is partially occluded |
| truncated | bool | Whether object is truncated at image edge |

## Product Categories (10 classes)

cereal_box, beverage_can, water_bottle, snack_bag, dairy_carton, cleaning_product, frozen_food, condiment_jar, bread_loaf, canned_goods

## Usage

Train an object detection model to localize and classify retail products. Predictions should include bounding boxes and class labels per image. Evaluated using mean Average Precision (mAP) at IoU threshold 0.50.
