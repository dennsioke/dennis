"""
grade.py - Grades predictions for medical text classification.
Usage: python grade.py --predictions predictions.csv
"""

import argparse
import csv

LABELS = ["cardiovascular", "respiratory", "neurological", "gastrointestinal",
          "musculoskeletal", "endocrine", "dermatological"]


def load_csv(path, key, val):
    with open(path, "r", encoding="utf-8") as f:
        return {r[key]: r[val] for r in csv.DictReader(f)}


def f1_macro(y_true, y_pred):
    f1s = {}
    for label in LABELS:
        tp = sum(1 for t, p in zip(y_true, y_pred) if t == label and p == label)
        fp = sum(1 for t, p in zip(y_true, y_pred) if t != label and p == label)
        fn = sum(1 for t, p in zip(y_true, y_pred) if t == label and p != label)
        prec = tp / (tp + fp) if (tp + fp) else 0
        rec = tp / (tp + fn) if (tp + fn) else 0
        f1s[label] = 2 * prec * rec / (prec + rec) if (prec + rec) else 0
    return f1s


def grade(pred_path, ans_path="dataset/private/answers.csv"):
    answers = load_csv(ans_path, "note_id", "condition")
    preds = load_csv(pred_path, "note_id", "predicted_condition")

    y_true, y_pred = [], []
    for nid, true in answers.items():
        y_true.append(true)
        y_pred.append(preds.get(nid, "__missing__"))

    f1s = f1_macro(y_true, y_pred)
    macro = sum(f1s.values()) / len(f1s)

    print("\n=== Grade Results ===")
    for label, score in sorted(f1s.items()):
        print(f"  {label:20s}: {score:.4f}")
    print(f"\nMacro F1: {macro:.4f}")

    pts = 0
    if macro >= 0.65: pts += 25; print("[PASS] Rubric 1 +25")
    if macro >= 0.75: pts += 35; print("[PASS] Rubric 2 +35")
    if macro >= 0.82: pts += 25; print("[PASS] Rubric 3 +25")
    if macro >= 0.87: pts += 15; print("[PASS] Rubric 4 +15")
    print(f"\nTotal: {pts}/100")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--predictions", required=True)
    p.add_argument("--answers", default="dataset/private/answers.csv")
    args = p.parse_args()
    grade(args.predictions, args.answers)
