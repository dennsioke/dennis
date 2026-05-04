"""
solution.py - Reference solution: fine-tune T5-small for abstractive news summarization.
"""

import csv
import warnings

warnings.filterwarnings("ignore")

TRAIN_FILE = "dataset/public/train.csv"
TEST_FILE = "dataset/public/test.csv"
OUTPUT_FILE = "predictions.csv"
MODEL_NAME = "t5-small"
MAX_INPUT_LEN = 512
MAX_TARGET_LEN = 80
EPOCHS = 3
BATCH_SIZE = 8
LR = 3e-4


def load_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    try:
        import torch
        from torch.utils.data import Dataset, DataLoader
        from transformers import T5Tokenizer, T5ForConditionalGeneration
        from torch.optim import AdamW
    except ImportError:
        print("transformers and torch required. Install: pip install transformers torch sentencepiece")
        return

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)

    train_rows = load_csv(TRAIN_FILE)
    test_rows = load_csv(TEST_FILE)

    class SumDataset(Dataset):
        def __init__(self, rows, has_labels=True):
            self.rows = rows
            self.has_labels = has_labels

        def __len__(self):
            return len(self.rows)

        def __getitem__(self, idx):
            row = self.rows[idx]
            inp = "summarize: " + row["article_text"]
            enc = tokenizer(inp, truncation=True, max_length=MAX_INPUT_LEN,
                            padding="max_length", return_tensors="pt")
            item = {k: v.squeeze(0) for k, v in enc.items()}
            if self.has_labels:
                with tokenizer.as_target_tokenizer():
                    tgt = tokenizer(row["summary"], truncation=True, max_length=MAX_TARGET_LEN,
                                    padding="max_length", return_tensors="pt")
                labels = tgt["input_ids"].squeeze(0)
                labels[labels == tokenizer.pad_token_id] = -100
                item["labels"] = labels
            return item

    train_dl = DataLoader(SumDataset(train_rows), batch_size=BATCH_SIZE, shuffle=True)
    optimizer = AdamW(model.parameters(), lr=LR)

    model.train()
    for epoch in range(EPOCHS):
        total_loss = 0
        for batch in train_dl:
            batch = {k: v.to(device) for k, v in batch.items()}
            loss = model(**batch).loss
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}/{EPOCHS} | Loss: {total_loss/len(train_dl):.4f}")

    model.eval()
    results = []
    for row in test_rows:
        inp = "summarize: " + row["article_text"]
        enc = tokenizer(inp, return_tensors="pt", truncation=True,
                        max_length=MAX_INPUT_LEN).to(device)
        with torch.no_grad():
            ids = model.generate(**enc, max_new_tokens=MAX_TARGET_LEN,
                                  num_beams=4, early_stopping=True)
        summary = tokenizer.decode(ids[0], skip_special_tokens=True)
        results.append({"article_id": row["article_id"], "predicted_summary": summary})

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["article_id", "predicted_summary"])
        w.writeheader()
        w.writerows(results)

    print(f"Saved {len(results)} summaries -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
