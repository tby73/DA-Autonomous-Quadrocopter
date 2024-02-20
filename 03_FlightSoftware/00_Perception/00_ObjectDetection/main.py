import cv2
import numpy as np

from objectdetector import ObjectDetector

# camera variables
MICROSOFT_HWB1_CAM = 0
VIDEO_SOURCE_0 = "video_0006.mp4"
VIDEO_SOURCE_1 = ""

# YOLOv8 model path
YOLOV8_OBJ_D_MODEL_PATH = "yolo-weights/yolov8n.pt"

def main():
    video_cap = cv2.VideoCapture(MICROSOFT_HWB1_CAM)

    while True:
        _, input_frame = video_cap.read()
        detector = ObjectDetector(input_frame, YOLOV8_OBJ_D_MODEL_PATH)
        output = detector.Detect()

        cv2.imshow("AutoQuad FS-CV - Object Detection", cv2.cvtColor(output, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(20) & 0xff == ord("q"):
            break

    video_cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

