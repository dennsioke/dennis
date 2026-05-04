"""grade.py - Computes mAP@0.50 for object detection predictions."""

import argparse, csv
from collections import defaultdict


def iou(b1, b2):
    x1 = max(b1[0], b2[0]); y1 = max(b1[1], b2[1])
    x2 = min(b1[0]+b1[2], b2[0]+b2[2]); y2 = min(b1[1]+b1[3], b2[1]+b2[3])
    inter = max(0, x2-x1) * max(0, y2-y1)
    union = b1[2]*b1[3] + b2[2]*b2[3] - inter
    return inter / union if union > 0 else 0


def compute_ap(tp_list, n_gt):
    if n_gt == 0:
        return 0.0
    tp_cum, fp_cum = 0, 0
    precisions, recalls = [], []
    for tp in tp_list:
        if tp: tp_cum += 1
        else: fp_cum += 1
        precisions.append(tp_cum / (tp_cum + fp_cum))
        recalls.append(tp_cum / n_gt)
    ap = 0.0
    prev_recall = 0
    for p, r in zip(precisions, recalls):
        ap += p * (r - prev_recall)
        prev_recall = r
    return ap


def grade(pred_path, ans_path="dataset/private/test_annotations.csv", iou_thresh=0.50):
    gt_by_img_cat = defaultdict(list)
    with open(ans_path,"r",encoding="utf-8") as f:
        for row in csv.DictReader(f):
            b = (float(row["bbox_x"]), float(row["bbox_y"]), float(row["bbox_w"]), float(row["bbox_h"]))
            gt_by_img_cat[(row["image_id"], row["category"])].append(b)

    preds_by_cat = defaultdict(list)
    with open(pred_path,"r",encoding="utf-8") as f:
        for row in csv.DictReader(f):
            b = (float(row["bbox_x"]), float(row["bbox_y"]), float(row["bbox_w"]), float(row["bbox_h"]))
            preds_by_cat[row["category"]].append((float(row["score"]), row["image_id"], b))

    CATS = ["cereal_box","beverage_can","water_bottle","snack_bag","dairy_carton",
            "cleaning_product","frozen_food","condiment_jar","bread_loaf","canned_goods"]

    ap_scores = {}
    for cat in CATS:
        cat_preds = sorted(preds_by_cat[cat], key=lambda x: -x[0])
        matched = defaultdict(set)
        tp_list = []
        n_gt = sum(len(v) for k, v in gt_by_img_cat.items() if k[1] == cat)

        for score, img_id, pb in cat_preds:
            gts = gt_by_img_cat.get((img_id, cat), [])
            best_iou, best_j = 0, -1
            for j, gb in enumerate(gts):
                if j in matched[(img_id, cat)]: continue
                i = iou(pb, gb)
                if i > best_iou: best_iou, best_j = i, j
            if best_iou >= iou_thresh:
                matched[(img_id, cat)].add(best_j)
                tp_list.append(True)
            else:
                tp_list.append(False)

        ap_scores[cat] = compute_ap(tp_list, n_gt)

    mAP = sum(ap_scores.values()) / len(ap_scores)
    print("\n=== Object Detection Results ===")
    for cat, ap in sorted(ap_scores.items()): print(f"  {cat:20s}: AP={ap:.4f}")
    print(f"\nmAP@0.50: {mAP:.4f}")

    pts = 0
    if mAP >= 0.30: pts += 25; print("[PASS] R1 +25")
    if mAP >= 0.45: pts += 30; print("[PASS] R2 +30")
    if mAP >= 0.60: pts += 25; print("[PASS] R3 +25")
    if mAP >= 0.72: pts += 20; print("[PASS] R4 +20")
    print(f"\nTotal: {pts}/100")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--predictions", required=True)
    p.add_argument("--answers", default="dataset/private/test_annotations.csv")
    args = p.parse_args()
    grade(args.predictions, args.answers)
