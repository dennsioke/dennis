"""solution.py - Random Forest classifier on plant disease image features."""

import csv
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np

FEATURE_COLS = ["leaf_color_r", "leaf_color_g", "leaf_color_b", "texture_contrast",
                "texture_homogeneity", "lesion_area_pct", "image_width", "image_height", "brightness"]
CROP_ENCODE = {"tomato": 0, "potato": 1, "corn": 2, "wheat": 3, "grape": 4}


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def to_features(rows):
    X = []
    for row in rows:
        feats = [float(row[c]) for c in FEATURE_COLS]
        feats.append(CROP_ENCODE.get(row.get("crop_type", ""), -1))
        X.append(feats)
    return np.array(X)


def main():
    train = load("dataset/public/train.csv")
    test = load("dataset/public/test.csv")

    X_train = to_features(train)
    y_train = [r["disease"] for r in train]
    X_test = to_features(test)
    test_ids = [r["image_id"] for r in test]

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", RandomForestClassifier(n_estimators=300, class_weight="balanced", n_jobs=-1, random_state=42)),
    ])
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    with open("predictions.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["image_id", "predicted_disease"])
        w.writeheader()
        for iid, pred in zip(test_ids, preds):
            w.writerow({"image_id": iid, "predicted_disease": pred})

    print(f"Saved {len(preds)} predictions -> predictions.csv")


if __name__ == "__main__":
    main()
