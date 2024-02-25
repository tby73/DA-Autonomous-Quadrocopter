import cv2
import pyrealsense2 as rs

from l515 import L515

# frame vars
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

def main():
    lidar_cam = L515(FRAME_WIDTH, FRAME_HEIGHT)

    while True:
        colored_out = cv2.cvtColor(lidar_cam.GetRGB(), cv2.COLOR_RGB2BGR)

        cv2.imshow("AutoQuad FS-CV - L515 RGB Output", colored_out)

        if cv2.waitKey(20) & 0xff == ord("q"):
            break

if __name__ == "__main__":
    main()



