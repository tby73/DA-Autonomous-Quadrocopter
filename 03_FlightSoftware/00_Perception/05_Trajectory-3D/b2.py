import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pyrealsense2 as rs

# Constants for sensor fusion
alpha = 0.98  # Complementary filter constant
dt = 0.1      # Time step

# Initialize the Realsense pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.accel)
config.enable_stream(rs.stream.gyro)
pipeline.start(config)

# Initialize figure and axes for 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('L515 Camera Trajectory')

# Initialize empty lists to store camera trajectory data
x_data, y_data, z_data = [], [], []

# Initialize orientation estimate
orientation = np.array([0.0, 0.0, 0.0])  # Initial orientation

try:
    while True:
        # Wait for a new frame from the camera
        frames = pipeline.wait_for_frames()
        accel_frame = frames.first_or_default(rs.stream.accel)
        gyro_frame = frames.first_or_default(rs.stream.gyro)

        if accel_frame and gyro_frame:
            accel_data = accel_frame.as_motion_frame().get_motion_data()
            gyro_data = gyro_frame.as_motion_frame().get_motion_data()

            # Extract acceleration and gyroscope data
            accel = np.array([accel_data.x, accel_data.y, accel_data.z])
            gyro = np.array([gyro_data.x, gyro_data.y, gyro_data.z])

            # Sensor fusion using complementary filter
            gyro_scaled = gyro * dt
            orientation += gyro_scaled
            orientation = alpha * (orientation + gyro_scaled) + (1 - alpha) * accel

            # Update the camera trajectory data
            x_data.append(orientation[0])
            y_data.append(orientation[1])
            z_data.append(orientation[2])

            # Update the plot
            ax.plot3D(x_data, y_data, z_data, 'blue')
            plt.draw()
            plt.pause(0.2)

except KeyboardInterrupt:
    # Stop the pipeline and close the plot
    pipeline.stop()
    plt.close()
