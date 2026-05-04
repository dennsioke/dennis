# Medical NLP BERT Fine-Tuning Dataset

## Overview

This dataset contains synthetic clinical notes and medical text records labeled with medical condition categories. It is designed for fine-tuning pre-trained language models on medical text classification tasks.

## Dataset Details

- **Title:** Healthcare Clinical Notes Medical Text Fine-Tuning Dataset
- **License:** CC0 Public Domain
- **Source:** Synthetic
- **Format:** CSV
- **Size:** ~20,000 records

## Schema

| Column | Type | Description |
|--------|------|-------------|
| note_id | int | Unique clinical note identifier |
| text | string | Clinical note text (50-400 words) |
| condition | string | Medical condition category label |
| specialty | string | Medical specialty (e.g., cardiology) |
| note_length | int | Word count of the note |
| has_medication | bool | Whether note mentions medications |
| has_procedure | bool | Whether note mentions procedures |

## Class Distribution

| Condition | Count |
|-----------|-------|
| cardiovascular | 4,000 |
| respiratory | 3,500 |
| neurological | 3,000 |
| gastrointestinal | 3,000 |
| musculoskeletal | 2,500 |
| endocrine | 2,000 |
| dermatological | 2,000 |

## Generation Notes

Notes contain realistic medical terminology, abbreviations, and clinical phrasing. Designed to challenge models that have not been domain-adapted.

## Usage

Fine-tune a pre-trained transformer model (e.g., BERT, BioBERT, ClinicalBERT) on the training split and evaluate on the test split using macro F1.
