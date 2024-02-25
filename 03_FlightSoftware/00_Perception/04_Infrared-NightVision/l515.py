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
        self.config.enable_stream(rs.stream.infrared, self.L515_CONFIG_WIDTH, self.L515_CONFIG_HEIGHT, rs.format.y8, 30)

        self.pipeline.start(self.config)

    def GetInfrared8(self):
        frames = self.pipeline.wait_for_frames()

        # retrieve and process IR-Frame
        ir_frame = frames.get_infrared_frame()
        ir_image = np.asanyarray(ir_frame.get_data())
        ir_image = cv2.resize(ir_image, (self.output_width, self.output_height), interpolation=cv2.INTER_NEAREST)

        return ir_image
    
