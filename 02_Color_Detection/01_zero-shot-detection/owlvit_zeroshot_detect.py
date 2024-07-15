from transformers import pipeline
from PIL import Image
from PIL import ImageDraw
import cv2


device = 'cuda'
checkpoint = "google/owlv2-base-patch16-ensemble"
detector = pipeline(model=checkpoint, device=device, task="zero-shot-object-detection")

image = Image.open('colors3.jpg')

predictions = detector(
    image,
    candidate_labels=['red', 'green', 'blue', 'orange', 'yellow']
)

draw = ImageDraw.Draw(image)

for prediction in predictions:
    box = prediction["box"]
    label = prediction["label"]
    score = prediction["score"]

    xmin, ymin, xmax, ymax = box.values()
    draw.rectangle((xmin, ymin, xmax, ymax), outline="red", width=10)
    draw.text((xmin, ymin), f"{label}: {round(score,2)}", fill="white")

image.save('output.jpg')
