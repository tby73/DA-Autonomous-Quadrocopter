import pyrealsense2 as rs
import cv2
import numpy as np

class L515:
    def __init__(self, output_width, output_height) -> None:
        # config dims
        self.L515_CONFIG_WIDTH = 320
        self.L515_CONFIG_HEIGHT = 240

        # output dims 
        self.output_width = output_width
        self.output_height = output_height

        # L515-config
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.depth, self.L515_CONFIG_WIDTH, self.L515_CONFIG_HEIGHT, rs.format.z16, 30)

        self.pipeline.start(self.config)

    def GetDepth16(self):
        # get depth information frames
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()

        # process depth map
        depth_map = np.asanyarray(depth_frame.get_data())
        depth_map = cv2.applyColorMap(cv2.convertScaleAbs(depth_map, alpha=0.03), cv2.COLORMAP_JET)
        depth_map = cv2.resize(depth_map, (self.output_width, self.output_height), interpolation=cv2.INTER_NEAREST)

        return depth_map
    
