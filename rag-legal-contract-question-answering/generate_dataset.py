"""
generate_dataset.py - Generates synthetic legal contracts and Q&A pairs.
Output: dataset/contracts.csv, dataset/questions.csv
"""

import csv
import json
import os
import random
from datetime import date, timedelta

random.seed(42)

CONTRACT_TYPES = ["NDA", "employment", "lease", "service", "partnership"]

CLAUSE_TEMPLATES = {
    "termination": [
        "Either party may terminate this Agreement with {n} days written notice.",
        "This Agreement shall terminate automatically upon {event}.",
        "Termination for cause requires written notice and a {n}-day cure period.",
    ],
    "payment": [
        "Payment of {amount} USD shall be due within {n} days of invoice.",
        "Monthly retainer of {amount} USD is payable on the first business day of each month.",
        "Late payments shall accrue interest at {rate}% per annum.",
    ],
    "confidentiality": [
        "Each party agrees to keep Confidential Information strictly confidential for {n} years.",
        "Confidential Information must not be disclosed to third parties without prior written consent.",
        "The confidentiality obligations survive termination for a period of {n} years.",
    ],
    "liability": [
        "In no event shall either party be liable for indirect or consequential damages.",
        "Total liability under this Agreement shall not exceed {amount} USD.",
        "Each party indemnifies the other against claims arising from its own negligence.",
    ],
    "dispute_resolution": [
        "Disputes shall be resolved by binding arbitration in {city}.",
        "The parties agree to mediation before pursuing litigation.",
        "Any dispute shall be subject to the exclusive jurisdiction of the courts of {state}.",
    ],
    "intellectual_property": [
        "All work product created under this Agreement is owned by {party}.",
        "Each party retains ownership of its pre-existing intellectual property.",
        "Licensee is granted a non-exclusive, non-transferable license to use the software.",
    ],
    "governing_law": [
        "This Agreement shall be governed by the laws of {state}.",
        "The parties consent to jurisdiction in {city}, {state}.",
        "This Agreement is subject to the laws of the State of {state}, without regard to conflict of law principles.",
    ],
    "indemnification": [
        "{party} shall indemnify and hold harmless the other party from claims arising from its breach.",
        "Each party agrees to indemnify the other for any third-party claims related to its representations.",
        "Indemnification obligations are capped at the total fees paid in the preceding {n} months.",
    ],
}

QUESTIONS_BY_CLAUSE = {
    "termination": ["How many days notice is required to terminate?", "Under what conditions does the agreement terminate?", "What is the cure period for termination for cause?"],
    "payment": ["When is payment due?", "What is the monthly retainer amount?", "What interest rate applies to late payments?"],
    "confidentiality": ["How long must confidential information be kept confidential?", "Can confidential information be shared with third parties?", "Do confidentiality obligations survive termination?"],
    "liability": ["What is the maximum liability under this agreement?", "Are indirect damages covered?", "Who bears liability for negligence?"],
    "dispute_resolution": ["Where will disputes be arbitrated?", "Is mediation required before litigation?", "Which courts have jurisdiction over disputes?"],
    "intellectual_property": ["Who owns work product created under this agreement?", "Does each party keep its pre-existing IP?", "What type of license is granted?"],
    "governing_law": ["Which state's laws govern this agreement?", "Where have the parties consented to jurisdiction?", "Does the agreement apply conflict of law principles?"],
    "indemnification": ["Who must indemnify whom?", "What triggers indemnification obligations?", "Is there a cap on indemnification?"],
}

STATES = ["California", "New York", "Texas", "Delaware", "Florida", "Washington"]
CITIES = ["San Francisco", "New York City", "Austin", "Wilmington", "Miami", "Seattle"]
PARTIES = ["Client", "Vendor", "Licensor", "Employer", "Lessor"]
EVENTS = ["expiration of the initial term", "mutual written agreement", "insolvency of either party"]


def fill(template):
    return template.format(
        n=random.choice([15, 30, 45, 60, 90]),
        amount=random.choice([5000, 10000, 50000, 100000, 500000]),
        rate=random.choice([1.5, 2.0, 3.0, 5.0]),
        city=random.choice(CITIES),
        state=random.choice(STATES),
        party=random.choice(PARTIES),
        event=random.choice(EVENTS),
    )


def build_contract(contract_id, contract_type):
    clauses = list(CLAUSE_TEMPLATES.keys())
    random.shuffle(clauses)
    selected = clauses[:random.randint(5, 8)]

    text_parts = [f"CONTRACT AGREEMENT\nType: {contract_type.upper()}\n\n"]
    clause_spans = {}

    for clause in selected:
        template = random.choice(CLAUSE_TEMPLATES[clause])
        text_snippet = fill(template)
        header = f"{clause.upper().replace('_', ' ')} CLAUSE\n"
        start = sum(len(p) for p in text_parts) + len(header)
        text_parts.append(header + text_snippet + "\n\n")
        clause_spans[clause] = (start, text_snippet)

    text = "".join(text_parts)
    effective = date(2022, 1, 1) + timedelta(days=random.randint(0, 730))

    return {
        "contract_id": contract_id,
        "contract_type": contract_type,
        "title": f"{contract_type.title()} Agreement No. {contract_id:04d}",
        "text": text,
        "word_count": len(text.split()),
        "effective_date": effective.isoformat(),
        "jurisdiction": random.choice(STATES),
    }, clause_spans


def generate():
    os.makedirs("dataset", exist_ok=True)
    contracts = []
    all_questions = []
    qid = 1

    for cid in range(1, 501):
        ctype = random.choice(CONTRACT_TYPES)
        contract, clause_spans = build_contract(cid, ctype)
        contracts.append(contract)

        for clause, (start, answer_text) in clause_spans.items():
            qs = QUESTIONS_BY_CLAUSE.get(clause, [])
            for q in random.sample(qs, min(len(qs), 2)):
                all_questions.append({
                    "question_id": qid,
                    "contract_id": cid,
                    "question": q,
                    "answer": answer_text,
                    "clause_type": clause,
                    "answer_start": start,
                })
                qid += 1

    contract_fields = ["contract_id", "contract_type", "title", "text", "word_count", "effective_date", "jurisdiction"]
    with open("dataset/contracts.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=contract_fields)
        w.writeheader(); w.writerows(contracts)

    q_fields = ["question_id", "contract_id", "question", "answer", "clause_type", "answer_start"]
    with open("dataset/questions.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=q_fields)
        w.writeheader(); w.writerows(all_questions)

    print(f"Generated {len(contracts)} contracts and {len(all_questions)} Q&A pairs")


if __name__ == "__main__":
    generate()
