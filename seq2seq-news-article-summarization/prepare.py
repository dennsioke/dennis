"""prepare.py - Splits news articles into train/test splits."""

import csv, os, random
random.seed(42)

def prepare():
    os.makedirs("dataset/public", exist_ok=True)
    os.makedirs("dataset/private", exist_ok=True)

    with open("dataset/news_articles.csv", "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    random.shuffle(rows)
    split = int(len(rows) * 0.80)
    train, test = rows[:split], rows[split:]

    train_fields = ["article_id", "topic", "headline", "article_text", "summary",
                    "article_word_count", "summary_word_count", "compression_ratio", "publish_date"]
    with open("dataset/public/train.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=train_fields); w.writeheader(); w.writerows(train)

    test_fields = ["article_id", "topic", "headline", "article_text", "article_word_count", "publish_date"]
    with open("dataset/public/test.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=test_fields); w.writeheader()
        for row in test: w.writerow({k: row[k] for k in test_fields})

    with open("dataset/private/answers.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["article_id", "summary", "topic"]); w.writeheader()
        for row in test: w.writerow({"article_id": row["article_id"], "summary": row["summary"], "topic": row["topic"]})

    print(f"Train: {len(train)} | Test: {len(test)}")

if __name__ == "__main__":
    prepare()
