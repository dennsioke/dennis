"""prepare.py - Splits plant disease dataset into train/test splits."""

import csv, os, random
random.seed(42)

def prepare():
    os.makedirs("dataset/public", exist_ok=True)
    os.makedirs("dataset/private", exist_ok=True)

    with open("dataset/plant_diseases.csv", "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    random.shuffle(rows)
    split = int(len(rows) * 0.80)
    train, test = rows[:split], rows[split:]

    train_fields = ["image_id", "crop_type", "disease", "severity", "leaf_color_r", "leaf_color_g",
                    "leaf_color_b", "texture_contrast", "texture_homogeneity", "lesion_area_pct",
                    "image_width", "image_height", "brightness"]
    with open("dataset/public/train.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=train_fields); w.writeheader(); w.writerows(train)

    test_fields = ["image_id", "crop_type", "severity", "leaf_color_r", "leaf_color_g",
                   "leaf_color_b", "texture_contrast", "texture_homogeneity", "lesion_area_pct",
                   "image_width", "image_height", "brightness"]
    with open("dataset/public/test.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=test_fields); w.writeheader()
        for row in test: w.writerow({k: row[k] for k in test_fields})

    with open("dataset/private/answers.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["image_id", "disease"]); w.writeheader()
        for row in test: w.writerow({"image_id": row["image_id"], "disease": row["disease"]})

    print(f"Train: {len(train)} | Test: {len(test)}")

if __name__ == "__main__":
    prepare()
