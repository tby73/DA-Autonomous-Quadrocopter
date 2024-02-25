import pyrealsense2 as rs
import numpy as np

class L515:
    def __init__(self, frame_width, frame_height) -> None:
        # output dims
        self.frame_width = frame_width
        self.frame_height = frame_height

        # L515-config 
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.color, self.frame_width, self.frame_height, rs.format.rgb8, 30)

        # start camera with applied configurations
        self.pipeline.start(self.config)

    def GetRGB(self):
        frames = self.pipeline.wait_for_frames()

        # select color frame from L515-output frames
        color_frame = frames.get_color_frame()
        color_image = np.asanyarray(color_frame.get_data())

        return color_image
    
