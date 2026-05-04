# Plant Disease Detection from Leaf Images

The dataset provides extracted visual features from plant leaf images across five crop types. Each sample represents a single leaf image and is labeled with one of eleven disease categories including a healthy class.

Your task is to build a classifier that predicts the disease class from the provided image features. Features include color channel statistics, texture descriptors, lesion area estimates, and image dimensions — all derived from leaf imagery collected in field conditions.

The challenge reflects real agricultural computer vision constraints: class imbalance between healthy and diseased samples, visual similarity between disease classes on different crops, and variation in severity. Models should generalize across crop types without being tuned to one specific plant.

Submit predictions as a CSV with columns `image_id` and `predicted_disease`. All eleven disease labels must be handled.

Evaluation uses macro-averaged F1 across all eleven classes. A score of 0.55 is required to pass the baseline. Top solutions should exceed 0.75 by leveraging crop-type context alongside visual features.

External plant disease datasets are not permitted. Pre-trained model architectures are allowed.
