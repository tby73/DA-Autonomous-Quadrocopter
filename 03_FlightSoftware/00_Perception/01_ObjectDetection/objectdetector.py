import cv2
import numpy as np

from ultralytics import YOLO
from labels import LABELS
from visualization_utils import Display

MODEL_PATH = "yolo-Weights/yolov8n.pt"
yolo_model = YOLO(MODEL_PATH)

def GetInputFrame(frame):
    return cv2.resize(frame, (640, 480), interpolation=cv2.INTER_LINEAR)

def GenerateCategoryColors(class_names):
    # generate random color for each category detected in image
    return np.random.randint(0, 255, size=(len(class_names) - 1, 3), dtype=np.uint8)

def Detect(frame):
    # get input frame and process detections
    frame = GetInputFrame(frame)
    detections = yolo_model(frame, stream=True)
    n_objects = 0

    category_colors = GenerateCategoryColors(LABELS)

    for d in detections:
        boxes = d.boxes

        for box in boxes:
            n_objects += 1

            # get bbox coordinates
            x, y, x1, y1 = box.xyxy[0]
            x, y, x1, y1 = int(x), int(y), int(x1), int(y1)

            class_id = int(box.cls[0])
            color = category_colors[class_id]

            # get width and height from coords
            w, h = (x1 - x), (y1 - y)

            # labeling
            label = LABELS[class_id]
            Display.BoundingBoxwithInfo(frame, f"{label}", 0.65, x, y, w, h, tuple(color.tolist()), 2)

    landing_label = (90, 420)

    # handle detections output for autonomous landing
    if n_objects == 0:
        cv2.putText(frame, "No Object near range [LANDING_CLEAR]", landing_label, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=(0, 255, 0))
    elif n_objects == 1:
        cv2.putText(frame, "1 Object near range [HOVER]", landing_label, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=(0, 0, 255))
    elif n_objects > 1:
        cv2.putText(frame, f"{n_objects} Objects near range [HOVER]", landing_label, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=(0, 0, 255))

    return frame

 