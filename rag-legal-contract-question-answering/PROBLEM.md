# Legal Contract Question Answering with RAG

The dataset contains 500 legal contracts across five contract types — NDAs, employment agreements, lease agreements, service contracts, and partnership agreements. Each contract is accompanied by ten natural language questions with ground truth answers extracted directly from the contract text.

Your task is to build a Retrieval-Augmented Generation pipeline that, given a question and its associated contract, retrieves the most relevant passage and generates a precise answer. Answers should be grounded in the contract text and should not rely on general legal knowledge.

The questions span eight clause types: termination, payment, confidentiality, liability, dispute resolution, intellectual property, governing law, and indemnification. Answering correctly requires understanding legal phrasing, identifying relevant clauses across varying document structures, and extracting precise spans rather than paraphrasing.

Submit predictions as a CSV with columns `question_id` and `predicted_answer`. Answers should be concise extracted spans, not full sentences unless the ground truth answer is a full sentence.

Evaluation uses token-level F1 score averaged across all questions. A score of 0.50 is required to pass the baseline. Top RAG systems with effective chunking, retrieval, and generation strategies should exceed 0.75.

Use of any large language model for generation is permitted. External legal databases are not allowed.
