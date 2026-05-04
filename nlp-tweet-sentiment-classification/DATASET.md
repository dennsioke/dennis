# NLP Tweet Sentiment Classification Dataset

## Overview

This dataset contains synthetic social media posts (tweets) labeled with sentiment categories for training and evaluating NLP classification models. The data simulates real-world microblogging content across five sentiment classes.

## Dataset Details

- **Title:** Social Media NLP Tweet Sentiment Classification Dataset
- **License:** CC0 Public Domain
- **Source:** Synthetic
- **Format:** CSV
- **Size:** ~50,000 records

## Schema

| Column | Type | Description |
|--------|------|-------------|
| tweet_id | int | Unique identifier |
| text | string | Raw tweet text (up to 280 characters) |
| sentiment | string | Label: positive, negative, neutral, angry, sad |
| language | string | ISO 639-1 language code |
| created_at | datetime | Timestamp of tweet |
| char_count | int | Number of characters in text |
| word_count | int | Number of words in text |
| has_hashtag | bool | Whether tweet contains hashtags |
| has_mention | bool | Whether tweet contains @mentions |
| has_url | bool | Whether tweet contains URLs |

## Class Distribution

| Sentiment | Count | Percentage |
|-----------|-------|------------|
| positive | 14,000 | 28% |
| negative | 12,000 | 24% |
| neutral | 13,000 | 26% |
| angry | 6,000 | 12% |
| sad | 5,000 | 10% |

## Generation Notes

Data was synthetically generated to reflect realistic tweet distributions including:
- Slang, abbreviations, and emojis
- Mixed-language content
- Varying text lengths
- Class imbalance to reflect real-world distributions

## Usage

This dataset is intended for use in NLP sentiment classification challenges. Participants should preprocess the text and train classification models evaluated against a held-out test set.
