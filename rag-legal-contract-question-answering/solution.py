"""
solution.py - Reference RAG solution using TF-IDF retrieval + extractive span selection.
"""

import csv
import re
import string
from collections import Counter

CONTRACTS_FILE = "dataset/public/contracts.csv"
QUESTIONS_FILE = "dataset/public/test_questions.csv"
OUTPUT_FILE = "predictions.csv"


def load_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def tokenize(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()


def tfidf_score(query_tokens, doc_tokens):
    query_set = set(query_tokens)
    doc_freq = Counter(doc_tokens)
    return sum(doc_freq[t] for t in query_set if t in doc_freq)


def chunk_text(text, chunk_size=100, overlap=20):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        start += chunk_size - overlap
    return chunks


def extract_answer(question, contract_text):
    """Retrieve best chunk and return it as the answer."""
    q_tokens = tokenize(question)
    chunks = chunk_text(contract_text)

    best_score = -1
    best_chunk = ""
    for chunk in chunks:
        score = tfidf_score(q_tokens, tokenize(chunk))
        if score > best_score:
            best_score = score
            best_chunk = chunk

    # Return the most relevant sentence from the best chunk
    sentences = re.split(r"[.!?\n]", best_chunk)
    best_sent = ""
    best_sent_score = -1
    for sent in sentences:
        if len(sent.strip()) < 10:
            continue
        s = tfidf_score(q_tokens, tokenize(sent))
        if s > best_sent_score:
            best_sent_score = s
            best_sent = sent.strip()

    return best_sent if best_sent else best_chunk[:200].strip()


def main():
    contracts = {str(c["contract_id"]): c["text"] for c in load_csv(CONTRACTS_FILE)}
    questions = load_csv(QUESTIONS_FILE)

    results = []
    for q in questions:
        contract_text = contracts.get(q["contract_id"], "")
        answer = extract_answer(q["question"], contract_text)
        results.append({"question_id": q["question_id"], "predicted_answer": answer})

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["question_id", "predicted_answer"])
        w.writeheader()
        w.writerows(results)

    print(f"Saved {len(results)} predictions -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
