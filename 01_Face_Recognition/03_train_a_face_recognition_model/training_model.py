import cv2
import face_recognition
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n-face.pt')  # Ensure you have a trained YOLOv8 face detection model

# Load the image
image_path = 'people.jpg'
image = cv2.imread(image_path)

# Perform inference with YOLOv8
results = model(image)

# List to store recognized face names
recognized_faces = []

# Known face encodings and their names
known_face_encodings = [
    # Add known face encodings here
    # face_recognition.face_encodings(face_recognition.load_image_file("person1.jpg"))[0],
    # face_recognition.face_encodings(face_recognition.load_image_file("person2.jpg"))[0],
]
known_face_names = [
    # Add names corresponding to the known face encodings
    # "Person 1",
    # "Person 2",
]

# Process YOLOv8 results
for result in results:
    boxes = result.boxes
    for box in boxes:
        # Extract the coordinates of the bounding box
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        confidence = box.conf[0]

        if confidence > 0.5:  # You can adjust the confidence threshold as needed
            # Extract the face region
            face_image = image[y1:y2, x1:x2]
            rgb_face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

            # Recognize the face
            face_encodings = face_recognition.face_encodings(rgb_face_image)
            if face_encodings:
                face_encoding = face_encodings[0]
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # Check if a match was found
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                recognized_faces.append(name)
                # Draw rectangle and label
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Display the image with the rectangles and labels
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
