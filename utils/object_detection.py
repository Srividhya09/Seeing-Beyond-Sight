from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
from collections import Counter

def detect_objects(image):
    model = YOLO("yolov5s.pt")  # Make sure this file exists

    # Convert PIL to OpenCV format
    opencv_image = np.array(image)
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)

    # Perform detection
    results = model.predict(opencv_image)
    detections = results[0].boxes.data
    class_names = results[0].names if hasattr(results[0], 'names') else {}

    object_names = []
    object_positions = {}

    img_width = opencv_image.shape[1]

    for detection in detections:
        x1, y1, x2, y2, conf, cls = map(float, detection[:6])
        class_id = int(cls)
        class_name = class_names.get(class_id, "object")

        object_names.append(class_name)

        # Determine position
        x_center = (x1 + x2) / 2
        if x_center < img_width / 3:
            position = "left"
        elif x_center > 2 * img_width / 3:
            position = "right"
        else:
            position = "center"

        if class_name not in object_positions:
            object_positions[class_name] = []
        object_positions[class_name].append(position)

        # Draw box and label
        label = f"{class_name} {conf:.2f}"
        cv2.rectangle(opencv_image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(opencv_image, label, (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Count each object
    object_counts = Counter(object_names)

    # Convert image back to PIL format
    detected_image = Image.fromarray(cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB))

    return detected_image, object_counts, object_positions
