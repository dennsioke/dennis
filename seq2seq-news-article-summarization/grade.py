"""grade.py - Computes ROUGE scores for summarization predictions."""

import argparse
import csv
import re
import string
from collections import Counter


def normalize(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()


def rouge_n(pred_tokens, ref_tokens, n):
    def ngrams(tokens, n):
        return Counter(tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1))
    pred_ng = ngrams(pred_tokens, n)
    ref_ng = ngrams(ref_tokens, n)
    common = pred_ng & ref_ng
    num_same = sum(common.values())
    if num_same == 0:
        return 0.0, 0.0, 0.0
    precision = num_same / sum(pred_ng.values())
    recall = num_same / sum(ref_ng.values())
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0
    return precision, recall, f1


def lcs_length(x, y):
    # Fast LCS approximation using set intersection
    x_set = set(x)
    y_set = set(y)
    common = x_set & y_set
    return sum(1 for t in x if t in common)


def rouge_l(pred_tokens, ref_tokens):
    lcs = lcs_length(pred_tokens, ref_tokens)
    if lcs == 0 or not pred_tokens or not ref_tokens:
        return 0.0
    precision = lcs / len(pred_tokens)
    recall = lcs / len(ref_tokens)
    return 2 * precision * recall / (precision + recall)


def grade(pred_path, ans_path="dataset/private/answers.csv"):
    with open(ans_path, "r", encoding="utf-8") as f:
        answers = {r["article_id"]: r for r in csv.DictReader(f)}
    with open(pred_path, "r", encoding="utf-8") as f:
        preds = {r["article_id"]: r["predicted_summary"] for r in csv.DictReader(f)}

    r1_scores, r2_scores, rl_scores = [], [], []
    topic_rl = {}

    for aid, ans in answers.items():
        pred_text = preds.get(aid, "")
        ref_text = ans["summary"]
        topic = ans.get("topic", "unknown")

        p_toks = normalize(pred_text)
        r_toks = normalize(ref_text)

        _, _, r1 = rouge_n(p_toks, r_toks, 1)
        _, _, r2 = rouge_n(p_toks, r_toks, 2)
        rl = rouge_l(p_toks, r_toks)

        r1_scores.append(r1)
        r2_scores.append(r2)
        rl_scores.append(rl)

        if topic not in topic_rl:
            topic_rl[topic] = []
        topic_rl[topic].append(rl)

    avg_r1 = sum(r1_scores) / len(r1_scores)
    avg_r2 = sum(r2_scores) / len(r2_scores)
    avg_rl = sum(rl_scores) / len(rl_scores)

    print(f"\n=== Summarization Results ===")
    print(f"ROUGE-1 F1: {avg_r1:.4f}")
    print(f"ROUGE-2 F1: {avg_r2:.4f}")
    print(f"ROUGE-L F1: {avg_rl:.4f}")
    print("\nPer-topic ROUGE-L:")
    for topic, scores in sorted(topic_rl.items()):
        print(f"  {topic:12s}: {sum(scores)/len(scores):.4f}")

    pts = 0
    if avg_rl >= 0.25: pts += 25; print("\n[PASS] R1 +25")
    if avg_rl >= 0.35 and avg_r1 >= 0.40 and avg_r2 >= 0.15: pts += 30; print("[PASS] R2 +30")
    if avg_rl >= 0.42: pts += 25; print("[PASS] R3 +25")
    all_above_040 = all(sum(s)/len(s) >= 0.40 for s in topic_rl.values())
    if avg_rl >= 0.48 and all_above_040: pts += 20; print("[PASS] R4 +20")
    print(f"\nTotal: {pts}/100")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--predictions", required=True)
    p.add_argument("--answers", default="dataset/private/answers.csv")
    args = p.parse_args()
    grade(args.predictions, args.answers)
