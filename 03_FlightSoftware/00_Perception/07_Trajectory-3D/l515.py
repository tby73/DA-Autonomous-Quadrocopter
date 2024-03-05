import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pyrealsense2 as rs

class L515:
    def __init__(self):
        self.pipeline = rs.pipeline()
        self.config = rs.config()

        # enable IMU
        self.config.enable_stream(rs.stream.gyro)
        self.config.enable_stream(rs.stream.accel)

        self.pipeline.start(self.config)

    def GetIMU(self):
        # get frames
        frames = self.pipeline.wait_for_frames()
        gyro_frame = frames.first_or_default(rs.stream.gyro)
        accel_frame = frames.first_or_default(rs.stream.accel)

        # processing into vectors
        if accel_frame and gyro_frame:
            gyro_data = gyro_frame.as_motion_frame().get_motion_data()
            accel_data = accel_frame.as_motion_frame().get_motion_data()

            gyro_3d = np.array([gyro_data.x, gyro_data.y, gyro_data.z])
            accel_3d = np.array([accel_data.x, accel_data.y, accel_data.z])

            return gyro_3d, accel_3d
        
