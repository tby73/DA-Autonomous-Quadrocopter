import cv2
import numpy as np

from semanticsegmentator import SemanticSegmentator

# camera variables
DEFAULT_CAMERA = 0
SECONDARY_CAMERA = 1
VIDEO_SOURCE_0 = ""

# images
IMAGE_TEST_PATH = "rt.jpg"

# model params
ENET_SEM_SEGMENT_MODEL_PATH = "enet-model.net"
OUTPUT_CLASSES_TXT = "classes.txt"

def VideoEval():
    video_cap = cv2.VideoCapture(DEFAULT_CAMERA)

    while True:
        _, input_frame = video_cap.read()
        sem_segmentator = SemanticSegmentator(input_frame, ENET_SEM_SEGMENT_MODEL_PATH, OUTPUT_CLASSES_TXT, set_default_colors=True)
        segmented_output = sem_segmentator.Segment()

        cv2.imshow("AutoQuad FS-CV - Semantic Segmentation", segmented_output)

        if cv2.waitKey(20) & 0xff == ord("q"):
            break

    video_cap.release()
    cv2.destroyAllWindows()

def ImageEval():
    input_image = cv2.imread(IMAGE_TEST_PATH)

    sem_segmentator = SemanticSegmentator(input_image, ENET_SEM_SEGMENT_MODEL_PATH, OUTPUT_CLASSES_TXT, set_default_colors=True)
    segmented_output = sem_segmentator.Segment()

    cv2.imshow("AutoQuad FS-CV - Semantic Segmentation", segmented_output)
    cv2.waitKey(0)

def main():
    ImageEval()

if __name__ == "__main__":
    main()

