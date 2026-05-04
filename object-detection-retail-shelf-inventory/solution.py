"""solution.py - Baseline detection: predict ground truth boxes with slight noise for testing."""

import csv
from collections import defaultdict
import random

random.seed(0)

TRAIN_ANN = "dataset/public/train_annotations.csv"
TEST_IMGS = "dataset/public/test_images.csv"
OUTPUT = "predictions.csv"

# Prior box sizes by category (learned from training data statistics)
CAT_PRIORS = {}


def load_priors():
    sizes = defaultdict(list)
    with open(TRAIN_ANN, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sizes[row["category"]].append((float(row["bbox_w"]), float(row["bbox_h"])))
    for cat, vals in sizes.items():
        avg_w = sum(v[0] for v in vals) / len(vals)
        avg_h = sum(v[1] for v in vals) / len(vals)
        CAT_PRIORS[cat] = (avg_w, avg_h)


def load_section_dist():
    """Learn category distribution per shelf section from training data."""
    from collections import Counter
    section_cat = defaultdict(Counter)
    img_section = {}
    with open("dataset/public/images.csv", "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            img_section[row["image_id"]] = row["shelf_section"]
    with open(TRAIN_ANN, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            section = img_section.get(row["image_id"], "grocery")
            section_cat[section][row["category"]] += 1
    return section_cat, img_section


CATS = ["cereal_box","beverage_can","water_bottle","snack_bag","dairy_carton",
        "cleaning_product","frozen_food","condiment_jar","bread_loaf","canned_goods"]


def predict_for_image(img_id, section, section_cat_dist):
    dist = section_cat_dist.get(section, {})
    total = sum(dist.values()) or 1
    results = []
    n_preds = random.randint(3, 8)
    for _ in range(n_preds):
        # Sample category by section distribution
        cats, weights = zip(*dist.items()) if dist else (CATS, [1]*len(CATS))
        cat = random.choices(list(cats), weights=list(weights))[0]
        pw, ph = CAT_PRIORS.get(cat, (0.10, 0.15))
        bw = pw * random.uniform(0.8, 1.2)
        bh = ph * random.uniform(0.8, 1.2)
        bx = random.uniform(0, max(0.001, 1.0 - bw))
        by = random.uniform(0, max(0.001, 1.0 - bh))
        score = random.uniform(0.4, 0.9)
        results.append({
            "image_id": img_id, "category": cat,
            "bbox_x": round(bx, 4), "bbox_y": round(by, 4),
            "bbox_w": round(bw, 4), "bbox_h": round(bh, 4),
            "score": round(score, 3),
        })
    return results


def main():
    load_priors()
    section_cat_dist, img_section = load_section_dist()

    with open(TEST_IMGS, "r", encoding="utf-8") as f:
        test_imgs = list(csv.DictReader(f))

    all_preds = []
    for img in test_imgs:
        section = img.get("shelf_section", "grocery")
        all_preds.extend(predict_for_image(img["image_id"], section, section_cat_dist))

    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["image_id","category","bbox_x","bbox_y","bbox_w","bbox_h","score"])
        w.writeheader(); w.writerows(all_preds)

    print(f"Saved {len(all_preds)} predictions -> {OUTPUT}")


if __name__ == "__main__":
    main()
