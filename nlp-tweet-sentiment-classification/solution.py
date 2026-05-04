"""
solution.py

Reference solution for NLP Tweet Sentiment Classification.
Uses TF-IDF features with a Logistic Regression classifier.
Outputs predictions to predictions.csv.
"""

import csv
import os
import re

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder


TRAIN_FILE = "dataset/public/train.csv"
TEST_FILE = "dataset/public/test.csv"
OUTPUT_FILE = "predictions.csv"


def load_csv(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def preprocess_text(text):
    """Basic text normalization for tweets."""
    text = text.lower()
    text = re.sub(r"http\S+", " URL ", text)
    text = re.sub(r"@\w+", " MENTION ", text)
    text = re.sub(r"#(\w+)", r" \1 ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def main():
    print("Loading data...")
    train_rows = load_csv(TRAIN_FILE)
    test_rows = load_csv(TEST_FILE)

    X_train = [preprocess_text(row["text"]) for row in train_rows]
    y_train = [row["sentiment"] for row in train_rows]

    X_test = [preprocess_text(row["text"]) for row in test_rows]
    test_ids = [row["tweet_id"] for row in test_rows]

    print("Training model...")
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            ngram_range=(1, 2),
            max_features=50000,
            sublinear_tf=True,
            min_df=2,
        )),
        ("clf", LogisticRegression(
            C=1.0,
            max_iter=1000,
            class_weight="balanced",
            multi_class="multinomial",
            solver="lbfgs",
        )),
    ])

    pipeline.fit(X_train, y_train)

    print("Generating predictions...")
    y_pred = pipeline.predict(X_test)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["tweet_id", "predicted_sentiment"])
        writer.writeheader()
        for tid, pred in zip(test_ids, y_pred):
            writer.writerow({"tweet_id": tid, "predicted_sentiment": pred})

    print(f"Predictions saved to {OUTPUT_FILE} ({len(y_pred)} rows)")


if __name__ == "__main__":
    main()
