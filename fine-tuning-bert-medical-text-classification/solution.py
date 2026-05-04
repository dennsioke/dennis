"""
solution.py - Reference solution: fine-tune BERT for medical text classification.
"""

import csv
import os
import warnings

warnings.filterwarnings("ignore")

TRAIN_FILE = "dataset/public/train.csv"
TEST_FILE = "dataset/public/test.csv"
OUTPUT_FILE = "predictions.csv"
MODEL_NAME = "dmis-lab/biobert-base-cased-v1.2"  # Falls back to bert-base-uncased if unavailable
LABELS = ["cardiovascular", "respiratory", "neurological", "gastrointestinal",
          "musculoskeletal", "endocrine", "dermatological"]
LABEL2ID = {l: i for i, l in enumerate(LABELS)}
ID2LABEL = {i: l for i, l in enumerate(LABELS)}
EPOCHS = 3
BATCH_SIZE = 16
MAX_LEN = 256
LR = 2e-5


def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    try:
        import torch
        from torch.utils.data import Dataset, DataLoader
        from transformers import AutoTokenizer, AutoModelForSequenceClassification
        from torch.optim import AdamW
        from transformers import get_linear_schedule_with_warmup
    except ImportError:
        print("transformers and torch are required. Install via: pip install transformers torch")
        return

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    train_rows = load_data(TRAIN_FILE)
    test_rows = load_data(TEST_FILE)

    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSequenceClassification.from_pretrained(
            MODEL_NAME, num_labels=len(LABELS), id2label=ID2LABEL, label2id=LABEL2ID
        )
    except Exception:
        print(f"Could not load {MODEL_NAME}, falling back to bert-base-uncased")
        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        model = AutoModelForSequenceClassification.from_pretrained(
            "bert-base-uncased", num_labels=len(LABELS), id2label=ID2LABEL, label2id=LABEL2ID
        )

    model.to(device)

    class NoteDataset(Dataset):
        def __init__(self, rows, has_labels=True):
            self.rows = rows
            self.has_labels = has_labels

        def __len__(self):
            return len(self.rows)

        def __getitem__(self, idx):
            row = self.rows[idx]
            enc = tokenizer(row["text"], truncation=True, max_length=MAX_LEN, padding="max_length", return_tensors="pt")
            item = {k: v.squeeze(0) for k, v in enc.items()}
            if self.has_labels:
                item["labels"] = torch.tensor(LABEL2ID[row["condition"]])
            return item

    train_ds = NoteDataset(train_rows, has_labels=True)
    train_dl = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)

    optimizer = AdamW(model.parameters(), lr=LR)
    scheduler = get_linear_schedule_with_warmup(optimizer, 0, len(train_dl) * EPOCHS)

    model.train()
    for epoch in range(EPOCHS):
        total_loss = 0
        for batch in train_dl:
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}/{EPOCHS} | Loss: {total_loss/len(train_dl):.4f}")

    model.eval()
    test_ds = NoteDataset(test_rows, has_labels=False)
    test_dl = DataLoader(test_ds, batch_size=BATCH_SIZE)

    preds = []
    with torch.no_grad():
        for batch in test_dl:
            batch = {k: v.to(device) for k, v in batch.items()}
            logits = model(**batch).logits
            preds.extend(logits.argmax(-1).cpu().numpy().tolist())

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["note_id", "predicted_condition"])
        w.writeheader()
        for row, pred in zip(test_rows, preds):
            w.writerow({"note_id": row["note_id"], "predicted_condition": ID2LABEL[pred]})

    print(f"Saved {len(preds)} predictions -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
