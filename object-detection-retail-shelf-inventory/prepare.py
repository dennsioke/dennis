"""prepare.py - Splits images into train/test sets."""

import csv, os, random
random.seed(42)

def prepare():
    os.makedirs("dataset/public", exist_ok=True)
    os.makedirs("dataset/private", exist_ok=True)

    with open("dataset/images.csv","r",encoding="utf-8") as f:
        images = list(csv.DictReader(f))
    with open("dataset/annotations.csv","r",encoding="utf-8") as f:
        annotations = list(csv.DictReader(f))

    random.shuffle(images)
    split = int(len(images) * 0.80)
    train_imgs = images[:split]
    test_imgs = images[split:]

    train_ids = {img["image_id"] for img in train_imgs}
    test_ids = {img["image_id"] for img in test_imgs}

    img_fields = ["image_id","filename","width","height","shelf_section","num_objects"]
    import shutil
    shutil.copy("dataset/images.csv","dataset/public/images.csv")

    train_anns = [a for a in annotations if a["image_id"] in train_ids]
    test_anns = [a for a in annotations if a["image_id"] in test_ids]

    ann_fields = ["annotation_id","image_id","category","bbox_x","bbox_y","bbox_w","bbox_h","confidence_gt","occluded","truncated"]
    with open("dataset/public/train_annotations.csv","w",newline="",encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=ann_fields); w.writeheader(); w.writerows(train_anns)

    test_img_fields = ["image_id","filename","width","height","shelf_section"]
    with open("dataset/public/test_images.csv","w",newline="",encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=test_img_fields); w.writeheader()
        for img in test_imgs: w.writerow({k: img[k] for k in test_img_fields})

    with open("dataset/private/test_annotations.csv","w",newline="",encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=ann_fields); w.writeheader(); w.writerows(test_anns)

    print(f"Train: {len(train_imgs)} images, {len(train_anns)} annotations")
    print(f"Test:  {len(test_imgs)} images, {len(test_anns)} annotations (private)")

if __name__ == "__main__":
    prepare()
