import pyrealsense2 as rs
import cv2

from l515 import L515

# display dims
OUTPUT_WIDTH = 640
OUTPUT_HEIGHT = 480

def main():
    lidar_cam = L515(OUTPUT_WIDTH, OUTPUT_HEIGHT)

    while True:
        depth_map = lidar_cam.GetDepth16()

        cv2.imshow("AutoQuad FS-CV - L515 Depth Map", depth_map)

        if cv2.waitKey(20) & 0xff == ord("q"):
            break

if __name__ == "__main__":
    main()

