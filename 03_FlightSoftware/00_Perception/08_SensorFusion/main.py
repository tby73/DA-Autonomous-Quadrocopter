import pyrealsense2 as rs
import cv2
import numpy as np
import matplotlib.pyplot as plt

from l515 import L515

OUTPUT_WIDTH = 640
OUTPUT_HEIGHT = 480

def StackImages(images: list):
    return np.concatenate(images, axis=1)

def main():
    lidar_cam = L515(output_width=OUTPUT_WIDTH, output_height=OUTPUT_HEIGHT)

    while True:
        rgb_frame = cv2.cvtColor(lidar_cam.GetRGB8(), cv2.COLOR_RGB2BGR)
        depth_map = lidar_cam.GetDepth16()
        ir_frame = lidar_cam.GetInfrared8()

        #cv2.imshow("AutoQuad FS-CV - L515 Outputs", depth_map)

        if cv2.waitKey(20) & 0xff == ord("q"):
            break

if __name__ == "__main__":
    main()





