# Rubrics - Legal Contract RAG Question Answering

## Rubric 1: Baseline RAG
**Points:** 25
**Criteria:** Average token F1 >= 0.50 across all 5,000 questions. Must use a retrieval component (not just a reader model).

## Rubric 2: Effective Retrieval
**Points:** 30
**Criteria:** Average token F1 >= 0.65. Retrieval correctly identifies the relevant clause in >= 70% of questions.

## Rubric 3: High-Precision Extraction
**Points:** 25
**Criteria:** Average token F1 >= 0.75. Exact match score >= 0.35 on clause-level answers.

## Rubric 4: Production-Quality RAG
**Points:** 20
**Criteria:** Average token F1 >= 0.85. Demonstrates effective chunking, reranking, or answer verification.

## Scoring Notes

- Predictions CSV must have columns: `question_id`, `predicted_answer`
- Token F1 is computed as the harmonic mean of precision and recall on unigram overlap (SQuAD-style)
- Answers are compared case-insensitively after punctuation normalization
- Missing predictions receive F1 = 0
- Total possible score: 100 points
