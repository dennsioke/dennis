"""
grade.py

Evaluates participant predictions against the ground truth answers.
Usage: python grade.py --predictions <path_to_predictions.csv> --answers <path_to_answers.csv>

Predictions CSV must have columns: tweet_id, predicted_sentiment
Outputs: macro-averaged F1 score and per-class breakdown
"""

import argparse
import csv
import sys
from collections import defaultdict


VALID_LABELS = {"positive", "negative", "neutral", "angry", "sad"}


def load_csv(path, key_col, val_col):
    data = {}
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row[key_col]] = row[val_col]
    return data


def compute_f1_per_class(y_true, y_pred, labels):
    stats = {label: {"tp": 0, "fp": 0, "fn": 0} for label in labels}
    for true, pred in zip(y_true, y_pred):
        if true == pred:
            stats[true]["tp"] += 1
        else:
            stats.get(pred, {})  # ignore unknown predictions
            if pred in stats:
                stats[pred]["fp"] += 1
            if true in stats:
                stats[true]["fn"] += 1

    f1_scores = {}
    for label, s in stats.items():
        precision = s["tp"] / (s["tp"] + s["fp"]) if (s["tp"] + s["fp"]) > 0 else 0.0
        recall = s["tp"] / (s["tp"] + s["fn"]) if (s["tp"] + s["fn"]) > 0 else 0.0
        if precision + recall > 0:
            f1_scores[label] = 2 * precision * recall / (precision + recall)
        else:
            f1_scores[label] = 0.0
    return f1_scores


def grade(predictions_path, answers_path):
    answers = load_csv(answers_path, "tweet_id", "sentiment")
    predictions = load_csv(predictions_path, "tweet_id", "predicted_sentiment")

    y_true = []
    y_pred = []
    missing = 0

    for tweet_id, true_label in answers.items():
        pred_label = predictions.get(tweet_id, None)
        if pred_label is None:
            missing += 1
            pred_label = "__missing__"
        y_true.append(true_label)
        y_pred.append(pred_label)

    f1_per_class = compute_f1_per_class(y_true, y_pred, list(VALID_LABELS))
    macro_f1 = sum(f1_per_class.values()) / len(f1_per_class)

    print(f"\n=== Grading Results ===")
    print(f"Total samples: {len(answers)}")
    print(f"Missing predictions: {missing}")
    print(f"\nPer-class F1 scores:")
    for label, score in sorted(f1_per_class.items()):
        print(f"  {label:12s}: {score:.4f}")
    print(f"\nMacro-averaged F1: {macro_f1:.4f}")

    # Rubric scoring
    score = 0
    if macro_f1 >= 0.60:
        score += 30
        print("\n[PASS] Rubric 1: Baseline (F1 >= 0.60) +30 pts")
    if macro_f1 >= 0.72:
        score += 40
        print("[PASS] Rubric 2: Competitive (F1 >= 0.72) +40 pts")
    if macro_f1 >= 0.78:
        score += 30
        print("[PASS] Rubric 3: Top-Tier (F1 >= 0.78) +30 pts")

    print(f"\nTotal Score: {score}/100")
    return score


def main():
    parser = argparse.ArgumentParser(description="Grade NLP sentiment classification predictions")
    parser.add_argument("--predictions", required=True, help="Path to predictions CSV")
    parser.add_argument("--answers", default="dataset/private/answers.csv", help="Path to answers CSV")
    args = parser.parse_args()
    grade(args.predictions, args.answers)


if __name__ == "__main__":
    main()
