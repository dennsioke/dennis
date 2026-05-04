# News Article Abstractive Summarization

The dataset contains 15,000 news articles from five topic domains — politics, technology, sports, health, and finance — each paired with a human-written reference summary of one to three sentences.

Your task is to build a sequence-to-sequence model that generates abstractive summaries for unseen news articles. A good summary should capture the main points of the article, be grammatically fluent, and be significantly shorter than the source text. The compression ratio of reference summaries averages around 0.15.

The challenge spans five topic domains with distinct vocabulary and summarization styles. Political articles require capturing key decisions and actors. Technology articles often involve technical announcements that must be made accessible. Sports summaries emphasize outcomes and key performers. Health and finance articles require accurate preservation of numerical facts.

Submit predictions as a CSV with columns `article_id` and `predicted_summary`. Each summary should be one to three sentences.

Evaluation uses ROUGE-L F1 score averaged across all test articles. A score of 0.25 is required to pass the baseline. Models fine-tuned on the training data with appropriate abstractive architecture should exceed 0.40.

External news datasets are not permitted. Pre-trained seq2seq model weights (T5, BART, PEGASUS) are allowed.
