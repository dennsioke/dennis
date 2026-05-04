"""
generate_dataset.py - Generates synthetic plant disease image features dataset.
Output: dataset/plant_diseases.csv
"""

import csv
import os
import random

random.seed(42)

CROP_DISEASES = {
    "tomato": ["healthy", "early_blight", "late_blight", "leaf_mold", "mosaic_virus"],
    "potato": ["healthy", "early_blight", "late_blight"],
    "corn": ["healthy", "gray_leaf_spot", "rust", "powdery_mildew"],
    "wheat": ["healthy", "rust", "septoria", "powdery_mildew"],
    "grape": ["healthy", "black_rot", "downy_mildew", "powdery_mildew"],
}

DISEASE_PROFILES = {
    "healthy": {"r": (80, 120), "g": (140, 190), "b": (60, 100), "lesion": (0, 2), "contrast": (0.1, 0.3)},
    "early_blight": {"r": (150, 200), "g": (120, 160), "b": (50, 90), "lesion": (10, 30), "contrast": (0.4, 0.7)},
    "late_blight": {"r": (100, 150), "g": (80, 120), "b": (60, 100), "lesion": (25, 60), "contrast": (0.5, 0.8)},
    "leaf_mold": {"r": (110, 150), "g": (100, 140), "b": (70, 110), "lesion": (15, 40), "contrast": (0.3, 0.6)},
    "mosaic_virus": {"r": (130, 180), "g": (150, 200), "b": (80, 120), "lesion": (5, 20), "contrast": (0.2, 0.5)},
    "gray_leaf_spot": {"r": (140, 180), "g": (130, 170), "b": (100, 140), "lesion": (20, 45), "contrast": (0.4, 0.7)},
    "rust": {"r": (190, 230), "g": (130, 170), "b": (60, 100), "lesion": (15, 50), "contrast": (0.5, 0.8)},
    "powdery_mildew": {"r": (200, 240), "g": (195, 235), "b": (190, 230), "lesion": (30, 70), "contrast": (0.2, 0.4)},
    "black_rot": {"r": (50, 90), "g": (50, 90), "b": (50, 90), "lesion": (40, 80), "contrast": (0.6, 0.9)},
    "downy_mildew": {"r": (120, 160), "g": (110, 150), "b": (90, 130), "lesion": (25, 55), "contrast": (0.4, 0.7)},
    "septoria": {"r": (160, 200), "g": (140, 180), "b": (100, 140), "lesion": (20, 45), "contrast": (0.5, 0.8)},
}

SEVERITY_WEIGHTS = {"mild": 0.4, "moderate": 0.4, "severe": 0.2}
TOTAL = 25000


def rnd(lo, hi):
    return round(random.uniform(lo, hi), 3)


def generate():
    os.makedirs("dataset", exist_ok=True)
    rows = []
    img_id = 1

    crops = list(CROP_DISEASES.keys())
    per_crop = TOTAL // len(crops)

    for crop in crops:
        diseases = CROP_DISEASES[crop]
        for i in range(per_crop):
            # Healthy samples are ~30%, diseased ~70%
            if random.random() < 0.30:
                disease = "healthy"
            else:
                disease = random.choice([d for d in diseases if d != "healthy"])

            severity = random.choices(list(SEVERITY_WEIGHTS.keys()), weights=list(SEVERITY_WEIGHTS.values()))[0]
            prof = DISEASE_PROFILES[disease]
            sev_mult = {"mild": 0.5, "moderate": 1.0, "severe": 1.5}[severity]

            lesion_lo = min(prof["lesion"][0] * sev_mult, 95)
            lesion_hi = min(prof["lesion"][1] * sev_mult, 99)

            r = rnd(*prof["r"])
            g = rnd(*prof["g"])
            b = rnd(*prof["b"])
            brightness = round((r + g + b) / 3, 3)
            contrast = rnd(*prof["contrast"])
            homogeneity = round(1 - contrast * 0.8 + random.uniform(-0.05, 0.05), 3)

            rows.append({
                "image_id": img_id,
                "crop_type": crop,
                "disease": disease,
                "severity": severity,
                "leaf_color_r": r,
                "leaf_color_g": g,
                "leaf_color_b": b,
                "texture_contrast": contrast,
                "texture_homogeneity": max(0, min(1, homogeneity)),
                "lesion_area_pct": round(rnd(lesion_lo, lesion_hi), 2),
                "image_width": random.choice([224, 256, 512]),
                "image_height": random.choice([224, 256, 512]),
                "brightness": brightness,
            })
            img_id += 1

    random.shuffle(rows)

    fields = ["image_id", "crop_type", "disease", "severity", "leaf_color_r", "leaf_color_g", "leaf_color_b",
              "texture_contrast", "texture_homogeneity", "lesion_area_pct", "image_width", "image_height", "brightness"]

    with open("dataset/plant_diseases.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f"Generated {len(rows)} samples -> dataset/plant_diseases.csv")


if __name__ == "__main__":
    generate()
