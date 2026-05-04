"""grade.py - Grades RAG answers using token-level F1 (SQuAD-style)."""

import argparse, csv, re, string
from collections import Counter


def normalize(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()


def token_f1(pred, truth):
    pred_toks = normalize(pred)
    truth_toks = normalize(truth)
    common = Counter(pred_toks) & Counter(truth_toks)
    num_same = sum(common.values())
    if num_same == 0:
        return 0.0
    precision = num_same / len(pred_toks)
    recall = num_same / len(truth_toks)
    return 2 * precision * recall / (precision + recall)


def grade(pred_path, ans_path="dataset/private/answers.csv"):
    with open(ans_path, "r", encoding="utf-8") as f:
        answers = {r["question_id"]: r["answer"] for r in csv.DictReader(f)}
    with open(pred_path, "r", encoding="utf-8") as f:
        preds = {r["question_id"]: r["predicted_answer"] for r in csv.DictReader(f)}

    scores = []
    for qid, truth in answers.items():
        pred = preds.get(qid, "")
        scores.append(token_f1(pred, truth))

    avg_f1 = sum(scores) / len(scores) if scores else 0
    exact_match = sum(1 for s in scores if s >= 0.999) / len(scores) if scores else 0

    print(f"\n=== RAG Legal QA Results ===")
    print(f"Questions evaluated: {len(scores)}")
    print(f"Average Token F1:   {avg_f1:.4f}")
    print(f"Exact Match Rate:   {exact_match:.4f}")

    pts = 0
    if avg_f1 >= 0.50: pts += 25; print("[PASS] R1 +25")
    if avg_f1 >= 0.65: pts += 30; print("[PASS] R2 +30")
    if avg_f1 >= 0.75: pts += 25; print("[PASS] R3 +25")
    if avg_f1 >= 0.85: pts += 20; print("[PASS] R4 +20")
    print(f"\nTotal: {pts}/100")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--predictions", required=True)
    p.add_argument("--answers", default="dataset/private/answers.csv")
    args = p.parse_args()
    grade(args.predictions, args.answers)
