"""grade.py - Grades plant disease detection predictions."""

import argparse, csv

LABELS = ["healthy", "early_blight", "late_blight", "leaf_mold", "mosaic_virus",
          "gray_leaf_spot", "rust", "powdery_mildew", "black_rot", "downy_mildew", "septoria"]


def load(path, key, val):
    with open(path, "r", encoding="utf-8") as f:
        return {r[key]: r[val] for r in csv.DictReader(f)}


def macro_f1(y_true, y_pred):
    f1s = {}
    for label in LABELS:
        tp = sum(t == p == label for t, p in zip(y_true, y_pred))
        fp = sum(t != label and p == label for t, p in zip(y_true, y_pred))
        fn = sum(t == label and p != label for t, p in zip(y_true, y_pred))
        pr = tp / (tp + fp) if tp + fp else 0
        re = tp / (tp + fn) if tp + fn else 0
        f1s[label] = 2 * pr * re / (pr + re) if pr + re else 0
    return f1s


def grade(pred_path, ans_path="dataset/private/answers.csv"):
    ans = load(ans_path, "image_id", "disease")
    pred = load(pred_path, "image_id", "predicted_disease")

    y_true = [ans[k] for k in ans]
    y_pred = [pred.get(k, "__missing__") for k in ans]

    f1s = macro_f1(y_true, y_pred)
    macro = sum(f1s.values()) / len(f1s)

    print("\n=== Plant Disease Detection Results ===")
    for l, s in sorted(f1s.items()): print(f"  {l:20s}: {s:.4f}")
    print(f"\nMacro F1: {macro:.4f}")

    pts = 0
    if macro >= 0.55: pts += 25; print("[PASS] R1 +25")
    if macro >= 0.65: pts += 30; print("[PASS] R2 +30")
    if macro >= 0.75: pts += 25; print("[PASS] R3 +25")
    if macro >= 0.82: pts += 20; print("[PASS] R4 +20")
    print(f"\nTotal: {pts}/100")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--predictions", required=True)
    p.add_argument("--answers", default="dataset/private/answers.csv")
    args = p.parse_args()
    grade(args.predictions, args.answers)
