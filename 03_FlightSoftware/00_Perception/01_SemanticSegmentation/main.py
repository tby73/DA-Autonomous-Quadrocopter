import cv2
import numpy as np

from semanticsegmentator import SemanticSegmentator

# camera variables
DEFAULT_CAMERA = 0
SECONDARY_CAMERA = 1
VIDEO_SOURCE_0 = ""

# model params
ENET_SEM_SEGMENT_MODEL_PATH = ""
OUTPUT_CLASSES_TXT = ""

def main():
    video_cap = cv2.VideoCapture(DEFAULT_CAMERA)

    while True:
        _, input_frame = video_cap.read()
        sem_segmentator = SemanticSegmentator(input_frame, ENET_SEM_SEGMENT_MODEL_PATH, OUTPUT_CLASSES_TXT)
        segmented_output = sem_segmentator.Segment()

        cv2.imshow("AutoQuad FS-CV - Semantic Segmentation", segmented_output)

        if cv2.waitKey(20) & 0xff == ord("q"):
            break

    video_cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

