# NLP Tweet Sentiment Classification

Build a sentiment classification model for short social media text. The dataset consists of tweets labeled across five sentiment classes: positive, negative, neutral, angry, and sad.

Your goal is to train a text classification model using the provided training data and generate predictions on the test set. The model must handle the characteristic challenges of microblogging text: informal language, abbreviations, hashtags, mentions, and emojis.

Predictions should be submitted as a CSV file with columns `tweet_id` and `predicted_sentiment`. All five classes must be predicted using their exact string labels.

The evaluation metric is macro-averaged F1 score across all five classes. A minimum macro F1 of 0.60 is required to pass the baseline rubric. Top scores should target above 0.75.

You are free to use any preprocessing strategy, feature extraction method, and classification algorithm. Pre-trained transformer models are permitted. External data is not allowed.
