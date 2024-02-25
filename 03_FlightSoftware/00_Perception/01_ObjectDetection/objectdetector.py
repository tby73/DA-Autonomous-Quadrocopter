import cv2
import numpy as np

from ultralytics import YOLO
from labels import LABELS

class ObjectDetector:
    def __init__(self, image, model_path) -> None:
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.model = YOLO(model_path)

    def GenerateCategoryColors(self):
        # generate a radnom RGB-Tuple with values in range 0-255
        return np.random.randint(0, 255, size=(len(LABELS) - 1, 3), dtype=np.uint8)
    
    def Detect(self):
        # load predictions
        detections = self.model(self.image, stream=True)
        category_colors = self.GenerateCategoryColors()

        for d in detections:
            boxes = d.boxes

            for box in boxes:
                # extract box coordinates
                x, y, x1, y1, = box.xyxy[0]
                x, y, x1, y1 = int(x), int(y), int(x1), int(y1)

                class_id = int(box.cls[0])
                color = category_colors[class_id]

                # visualize and mark
                label = LABELS[class_id]
                cv2.rectangle(self.image, (x, y), (x1, y1), color=tuple(color.tolist()), thickness=2)
                cv2.putText(self.image, label, (x, y - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=tuple(color.tolist()), lineType=cv2.LINE_AA)

        return cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
    

