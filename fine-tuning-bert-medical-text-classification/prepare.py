"""
prepare.py - Splits clinical_notes.csv into train/test splits.
"""

import csv
import os
import random

random.seed(42)

INPUT = "dataset/clinical_notes.csv"
PUBLIC_DIR = "dataset/public"
PRIVATE_DIR = "dataset/private"
TRAIN_RATIO = 0.80


def prepare():
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    os.makedirs(PRIVATE_DIR, exist_ok=True)

    with open(INPUT, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    random.shuffle(rows)
    split = int(len(rows) * TRAIN_RATIO)
    train, test = rows[:split], rows[split:]

    train_fields = ["note_id", "text", "condition", "specialty", "note_length", "has_medication", "has_procedure"]
    with open(f"{PUBLIC_DIR}/train.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=train_fields)
        w.writeheader()
        w.writerows(train)

    test_fields = ["note_id", "text", "specialty", "note_length", "has_medication", "has_procedure"]
    with open(f"{PUBLIC_DIR}/test.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=test_fields)
        w.writeheader()
        for row in test:
            w.writerow({k: row[k] for k in test_fields})

    with open(f"{PRIVATE_DIR}/answers.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["note_id", "condition"])
        w.writeheader()
        for row in test:
            w.writerow({"note_id": row["note_id"], "condition": row["condition"]})

    print(f"Train: {len(train)} | Test: {len(test)}")


if __name__ == "__main__":
    prepare()
