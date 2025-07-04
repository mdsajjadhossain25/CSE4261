import os
import shutil
import cv2

def convert_box(img_w, img_h, box):
    x1, y1, w, h = box
    x_center = (x1 + w / 2) / img_w
    y_center = (y1 + h / 2) / img_h
    w_norm = w / img_w
    h_norm = h / img_h
    return x_center, y_center, w_norm, h_norm

def process_split(split_name, img_dir, anno_file, out_img_dir, out_label_dir):
    os.makedirs(out_img_dir, exist_ok=True)
    if split_name != 'test':
        os.makedirs(out_label_dir, exist_ok=True)

    with open(anno_file, 'r') as f:
        lines = f.readlines()

    i = 0
    count = 0
    total_lines = len(lines)

    while i < total_lines:
        img_rel_path = lines[i].strip()
        i += 1

        # Skip non-JPG lines
        if not img_rel_path.endswith('.jpg'):
            continue

        img_path = os.path.join(img_dir, img_rel_path)
        if not os.path.exists(img_path):
            print(f"[{split_name}] Image not found: {img_path}")
            # Skip the expected number of lines (fail-safe)
            try:
                face_count = int(lines[i].strip())
                i += 1 + face_count
            except:
                pass
            continue

        # Copy image to flat output dir
        new_img_name = f"{count}.jpg"
        new_img_path = os.path.join(out_img_dir, new_img_name)
        shutil.copy(img_path, new_img_path)

        # Read image dimensions
        img = cv2.imread(img_path)
        if img is None:
            print(f"[{split_name}] Failed to read image: {img_path}")
            continue
        h, w = img.shape[:2]

        if split_name != 'test':
            try:
                face_count = int(lines[i].strip())
                i += 1
            except ValueError:
                print(f"[{split_name}] Invalid face count at line {i}: {lines[i]}")
                continue

            label_path = os.path.join(out_label_dir, f"{count}.txt")
            with open(label_path, 'w') as label_file:
                for _ in range(face_count):
                    if i >= total_lines:
                        break
                    bbox = list(map(int, lines[i].strip().split()[:4]))
                    i += 1

                    # Ignore invalid boxes
                    if bbox[2] <= 0 or bbox[3] <= 0:
                        continue

                    x, y, bw, bh = convert_box(w, h, bbox)
                    label_file.write(f"0 {x:.6f} {y:.6f} {bw:.6f} {bh:.6f}\n")

        count += 1

    print(f"[{split_name}] Processed {count} images.")

# === Update with your absolute paths ===
root_dir = "/home/sajjad/Desktop/42/Deep Learning/widerface"
output_dir = "/home/sajjad/Desktop/42/Deep Learning/widerface/widerface_yolo_format"

splits = [
    ("train",
     os.path.join(root_dir, "WIDER_train/images"),
     os.path.join(root_dir, "wider_face_split/wider_face_train_bbx_gt.txt")),

    ("val",
     os.path.join(root_dir, "WIDER_val/images"),
     os.path.join(root_dir, "wider_face_split/wider_face_val_bbx_gt.txt")),

    ("test",
     os.path.join(root_dir, "WIDER_test/images"),
     os.path.join(root_dir, "wider_face_split/wider_face_test_filelist.txt"))  # test has no labels
]

for split_name, img_dir, anno_file in splits:
    process_split(
        split_name,
        img_dir,
        anno_file,
        os.path.join(output_dir, "images", split_name),
        os.path.join(output_dir, "labels", split_name)
    )
