"""
generate_dataset.py - Generates synthetic retail shelf detection annotations.
Outputs: dataset/images.csv, dataset/annotations.csv
"""

import csv
import os
import random

random.seed(42)

CATEGORIES = ["cereal_box", "beverage_can", "water_bottle", "snack_bag", "dairy_carton",
              "cleaning_product", "frozen_food", "condiment_jar", "bread_loaf", "canned_goods"]

SECTION_BIAS = {
    "grocery": ["cereal_box", "canned_goods", "condiment_jar", "bread_loaf"],
    "beverages": ["beverage_can", "water_bottle"],
    "snacks": ["snack_bag", "cereal_box", "canned_goods"],
    "dairy": ["dairy_carton", "water_bottle"],
    "household": ["cleaning_product", "frozen_food", "condiment_jar"],
}

SIZES = {
    "cereal_box": (0.08, 0.18, 0.12, 0.30),
    "beverage_can": (0.03, 0.08, 0.06, 0.14),
    "water_bottle": (0.04, 0.10, 0.08, 0.25),
    "snack_bag": (0.06, 0.14, 0.08, 0.18),
    "dairy_carton": (0.06, 0.12, 0.10, 0.20),
    "cleaning_product": (0.05, 0.12, 0.08, 0.22),
    "frozen_food": (0.07, 0.15, 0.10, 0.22),
    "condiment_jar": (0.04, 0.09, 0.06, 0.15),
    "bread_loaf": (0.10, 0.20, 0.08, 0.18),
    "canned_goods": (0.04, 0.08, 0.06, 0.12),
}


def rnd(lo, hi):
    return round(random.uniform(lo, hi), 4)


def generate():
    os.makedirs("dataset", exist_ok=True)
    image_rows = []
    ann_rows = []
    ann_id = 1

    sections = list(SECTION_BIAS.keys())
    img_per_section = 2000

    for section in sections:
        biased_cats = SECTION_BIAS[section]
        for i in range(img_per_section):
            img_id = len(image_rows) + 1
            w, h = random.choice([640, 800, 1024, 1280]), random.choice([480, 600, 768, 960])
            n_obj = random.randint(3, 12)

            anns = []
            for _ in range(n_obj):
                # Bias category to section
                if random.random() < 0.70:
                    cat = random.choice(biased_cats)
                else:
                    cat = random.choice(CATEGORIES)

                wl, wh, hl, hh = SIZES[cat]
                bw = rnd(wl, wh)
                bh = rnd(hl, hh)
                bx = rnd(0, max(0.001, 1.0 - bw))
                by = rnd(0, max(0.001, 1.0 - bh))

                occluded = random.random() < 0.15
                truncated = (bx + bw > 0.95) or (by + bh > 0.95)

                anns.append({
                    "annotation_id": ann_id,
                    "image_id": img_id,
                    "category": cat,
                    "bbox_x": bx,
                    "bbox_y": by,
                    "bbox_w": bw,
                    "bbox_h": bh,
                    "confidence_gt": round(random.uniform(0.85, 1.0), 3),
                    "occluded": occluded,
                    "truncated": truncated,
                })
                ann_id += 1

            image_rows.append({
                "image_id": img_id,
                "filename": f"shelf_{section}_{i:04d}.jpg",
                "width": w,
                "height": h,
                "shelf_section": section,
                "num_objects": n_obj,
            })
            ann_rows.extend(anns)

    img_fields = ["image_id", "filename", "width", "height", "shelf_section", "num_objects"]
    with open("dataset/images.csv", "w", newline="", encoding="utf-8") as f:
        w_ = csv.DictWriter(f, fieldnames=img_fields); w_.writeheader(); w_.writerows(image_rows)

    ann_fields = ["annotation_id", "image_id", "category", "bbox_x", "bbox_y", "bbox_w", "bbox_h",
                  "confidence_gt", "occluded", "truncated"]
    with open("dataset/annotations.csv", "w", newline="", encoding="utf-8") as f:
        w_ = csv.DictWriter(f, fieldnames=ann_fields); w_.writeheader(); w_.writerows(ann_rows)

    print(f"Generated {len(image_rows)} images, {len(ann_rows)} annotations")


if __name__ == "__main__":
    generate()
