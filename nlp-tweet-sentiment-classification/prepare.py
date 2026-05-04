"""
prepare.py

Reads the raw dataset and splits it into public (train) and private (test) splits.
Writes:
  dataset/public/train.csv   - training data with labels
  dataset/private/test.csv   - test data without labels
  dataset/private/answers.csv - ground truth labels (hidden from participants)
"""

import csv
import os
import random

random.seed(42)

INPUT_FILE = "dataset/tweets.csv"
PUBLIC_DIR = "dataset/public"
PRIVATE_DIR = "dataset/private"
TRAIN_RATIO = 0.80


def prepare():
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    os.makedirs(PRIVATE_DIR, exist_ok=True)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    random.shuffle(rows)
    split = int(len(rows) * TRAIN_RATIO)
    train_rows = rows[:split]
    test_rows = rows[split:]

    # Train split - includes labels
    train_fields = ["tweet_id", "text", "sentiment", "language", "created_at",
                    "char_count", "word_count", "has_hashtag", "has_mention", "has_url"]
    with open(os.path.join(PUBLIC_DIR, "train.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=train_fields)
        writer.writeheader()
        writer.writerows(train_rows)

    # Test split - no labels
    test_fields = ["tweet_id", "text", "language", "created_at",
                   "char_count", "word_count", "has_hashtag", "has_mention", "has_url"]
    with open(os.path.join(PUBLIC_DIR, "test.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=test_fields)
        writer.writeheader()
        for row in test_rows:
            writer.writerow({k: row[k] for k in test_fields})

    # Ground truth answers (private)
    with open(os.path.join(PRIVATE_DIR, "answers.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["tweet_id", "sentiment"])
        writer.writeheader()
        for row in test_rows:
            writer.writerow({"tweet_id": row["tweet_id"], "sentiment": row["sentiment"]})

    print(f"Train: {len(train_rows)} rows -> {PUBLIC_DIR}/train.csv")
    print(f"Test:  {len(test_rows)} rows -> {PUBLIC_DIR}/test.csv")
    print(f"Answers: {len(test_rows)} rows -> {PRIVATE_DIR}/answers.csv")


if __name__ == "__main__":
    prepare()
