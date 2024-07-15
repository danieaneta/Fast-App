import cv2
import torch
from ultralytics import YOLO

model = YOLO('yolov8n-face.pt')
image_path = 'people.jpg'
image = cv2.imread(image_path)

results = model(image)

for result in results:
    boxes = results.boxes
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        confidence = box.conf[0]

        if confidence > 0.5:
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imwrite('output.jpg', image)