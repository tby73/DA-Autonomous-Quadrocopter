import pyrealsense2 as rs
import cv2

from l515 import L515

# output dims
OUTPUT_WIDTH = 640
OUTPUT_HEIGHT = 480

def main():
    lidar_cam = L515(OUTPUT_WIDTH, OUTPUT_HEIGHT)

    while True:
        ir_image = lidar_cam.GetInfrared8()

        cv2.imshow("AutoQuad FS-CV - Infrared Night Vision", ir_image)

        if cv2.waitKey(20) & 0xff == ord("q"):
            break

if __name__ == "__main__":
    main()

