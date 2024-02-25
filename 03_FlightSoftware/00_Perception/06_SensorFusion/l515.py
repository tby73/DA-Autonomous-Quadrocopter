import pyrealsense2 as rs
import cv2
import numpy as np
import matplotlib.pyplot as plt

class L515:
    def __init__(self, output_width, output_height) -> None:
        # config dims (LIDAR-IR)
        self.L515_LIDAR_IR_CONFIG_WIDTH = 320
        self.L515_LIDAR_IR_CONFIG_HEIGHT = 240

        # config dims (RGB)
        self.L515_COLOR_CONFIG_WIDTH = 640
        self.L515_COLOR_CONFIG_HEIGHT = 480

        # output dims
        self.output_width = output_width
        self.output_height = output_height

        # L515-config settings
        self.pipeline = rs.pipeline()
        self.config = rs.config()

        # enable RGB / LIDAR-Depth / Infrared-NV
        self.config.enable_stream(rs.stream.color, self.L515_COLOR_CONFIG_WIDTH, self.L515_COLOR_CONFIG_HEIGHT, rs.format.rgb8, 30)
        self.config.enable_stream(rs.stream.depth, self.L515_LIDAR_IR_CONFIG_WIDTH, self.L515_LIDAR_IR_CONFIG_HEIGHT, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.infrared, self.L515_LIDAR_IR_CONFIG_WIDTH, self.L515_LIDAR_IR_CONFIG_HEIGHT, rs.format.y8, 30)

        # apply settings
        self.pipeline.start(self.config)

    def GetRGB8(self):
        frames = self.pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        color_image = np.asanyarray(color_frame.get_data())
        color_image = cv2.resize(color_image, (self.output_width, self.output_height), interpolation=cv2.INTER_NEAREST)

        return color_image

    def GetDepth16(self):
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()

        depth_map = np.asanyarray(depth_frame.get_data())
        depth_map = cv2.applyColorMap(cv2.convertScaleAbs(depth_map, alpha=0.03), cv2.COLORMAP_JET)
        depth_map = cv2.resize(depth_map, (self.output_width, self.output_height), interpolation=cv2.INTER_NEAREST)

        return depth_map

    def GetInfrared8(self):
        frames = self.pipeline.wait_for_frames()
        ir_frame = frames.get_infrared_frame()

        ir_image = np.asanyarray(ir_frame.get_data())
        ir_image = cv2.resize(ir_image, (self.output_width, self.output_height), interpolation=cv2.INTER_NEAREST)
        
        return ir_image
    

