# Retail Shelf Product Detection

The dataset contains COCO-style bounding box annotations for retail shelf images across five store sections. Each image contains multiple product instances from ten categories: cereal boxes, beverage cans, water bottles, snack bags, dairy cartons, cleaning products, frozen food packages, condiment jars, bread loaves, and canned goods.

Your task is to train an object detection model that produces bounding box predictions and category labels for product instances in the test images. The evaluation reflects real retail inventory challenges: dense product arrangements, occlusion between adjacent items, truncated objects at image edges, and class imbalance across store sections.

Submit predictions as a CSV with columns `image_id`, `category`, `bbox_x`, `bbox_y`, `bbox_w`, `bbox_h`, and `score`. Coordinates are normalized to [0, 1] relative to image dimensions. Multiple rows per image are expected.

Evaluation uses mean Average Precision (mAP) at IoU 0.50. A mAP of 0.30 is required to pass the baseline. Top solutions using modern detection architectures (YOLO, Faster R-CNN, DETR) on feature-based representations should exceed 0.60.

Bounding box coordinates must be in [x, y, w, h] format where (x, y) is the top-left corner and (w, h) are width and height, all normalized. External retail datasets are not permitted.
