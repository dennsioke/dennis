"""prepare.py - Splits Q&A pairs into public train and private test sets."""

import csv, os, random
random.seed(42)

def prepare():
    os.makedirs("dataset/public", exist_ok=True)
    os.makedirs("dataset/private", exist_ok=True)

    with open("dataset/questions.csv", "r", encoding="utf-8") as f:
        questions = list(csv.DictReader(f))

    # Copy full contracts to public (needed for retrieval)
    import shutil
    shutil.copy("dataset/contracts.csv", "dataset/public/contracts.csv")

    random.shuffle(questions)
    split = int(len(questions) * 0.80)
    train, test = questions[:split], questions[split:]

    train_fields = ["question_id", "contract_id", "question", "answer", "clause_type", "answer_start"]
    with open("dataset/public/train_questions.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=train_fields); w.writeheader(); w.writerows(train)

    test_fields = ["question_id", "contract_id", "question", "clause_type"]
    with open("dataset/public/test_questions.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=test_fields); w.writeheader()
        for q in test: w.writerow({k: q[k] for k in test_fields})

    with open("dataset/private/answers.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["question_id", "answer"]); w.writeheader()
        for q in test: w.writerow({"question_id": q["question_id"], "answer": q["answer"]})

    print(f"Train: {len(train)} Q&A | Test: {len(test)} questions (answers hidden)")

if __name__ == "__main__":
    prepare()
