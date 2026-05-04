# Medical Text Classification via BERT Fine-Tuning

The dataset contains de-identified clinical notes from seven medical specialties. Each note is labeled with a primary condition category: cardiovascular, respiratory, neurological, gastrointestinal, musculoskeletal, endocrine, or dermatological.

Your task is to fine-tune a pre-trained transformer model on the provided training data and generate predictions for the test set. The model should classify each clinical note into its correct condition category.

The clinical notes contain domain-specific terminology, abbreviations common in medical practice, and varying note structures. A model without domain adaptation will struggle; the evaluation rewards fine-tuning choices that account for medical language.

Submit predictions as a CSV with columns `note_id` and `predicted_condition`. Labels must exactly match the category strings above.

Evaluation uses macro-averaged F1 score. You must achieve at least 0.65 to pass the baseline. Fine-tuned transformer models that leverage domain-adapted weights (e.g., BioBERT, ClinicalBERT) or custom training procedures are expected to score higher.

External medical datasets are not permitted. Pre-trained model weights from public repositories are allowed.
