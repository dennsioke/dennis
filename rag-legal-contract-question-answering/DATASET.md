# Legal Contract Question Answering RAG Dataset

## Overview

This dataset contains synthetic legal contract documents paired with question-answer pairs for evaluating Retrieval-Augmented Generation (RAG) pipelines. It simulates a real-world legal AI scenario where users ask questions about contract clauses.

## Dataset Details

- **Title:** Legal Industry Contract Documents RAG Question Answering Dataset
- **License:** CC0 Public Domain
- **Source:** Synthetic
- **Format:** CSV + JSON
- **Size:** 500 contracts, 5,000 Q&A pairs

## Files

| File | Description |
|------|-------------|
| contracts.csv | Contract documents with metadata |
| questions.csv | Questions with ground truth answers |

## Contracts Schema

| Column | Type | Description |
|--------|------|-------------|
| contract_id | int | Unique contract identifier |
| contract_type | string | Type: NDA, employment, lease, service, partnership |
| title | string | Contract title |
| text | string | Full contract text |
| word_count | int | Word count |
| effective_date | date | Contract effective date |
| jurisdiction | string | Legal jurisdiction |

## Questions Schema

| Column | Type | Description |
|--------|------|-------------|
| question_id | int | Unique question identifier |
| contract_id | int | Reference to contract |
| question | string | Natural language question |
| answer | string | Ground truth answer extracted from contract |
| clause_type | string | Type of clause the answer appears in |
| answer_start | int | Character offset of answer in contract text |

## Clause Types

termination, payment, confidentiality, liability, dispute_resolution, intellectual_property, governing_law, indemnification

## Usage

Build a RAG pipeline that retrieves relevant contract passages and generates accurate answers. Evaluate using exact match and F1 token overlap against ground truth answers.
