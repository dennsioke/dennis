# News Article Summarization Seq2Seq Dataset

## Overview

This synthetic dataset contains news articles paired with reference summaries for training and evaluating sequence-to-sequence text summarization models. It simulates real-world news summarization across five topic domains.

## Dataset Details

- **Title:** News Media Article Text Summarization Seq2Seq Dataset
- **License:** CC0 Public Domain
- **Source:** Synthetic
- **Format:** CSV
- **Size:** ~15,000 article-summary pairs

## Schema

| Column | Type | Description |
|--------|------|-------------|
| article_id | int | Unique article identifier |
| topic | string | News topic: politics, technology, sports, health, finance |
| headline | string | Article headline |
| article_text | string | Full article body (200-600 words) |
| summary | string | Reference summary (1-3 sentences, 30-80 words) |
| article_word_count | int | Word count of article |
| summary_word_count | int | Word count of summary |
| compression_ratio | float | summary_word_count / article_word_count |
| publish_date | date | Publication date |

## Topic Distribution

| Topic | Count |
|-------|-------|
| politics | 3,500 |
| technology | 3,000 |
| sports | 2,500 |
| health | 3,000 |
| finance | 3,000 |

## Usage

Fine-tune or prompt a sequence-to-sequence model (T5, BART, PEGASUS, or similar) to generate abstractive summaries. Evaluation uses ROUGE-1, ROUGE-2, and ROUGE-L scores against reference summaries.
