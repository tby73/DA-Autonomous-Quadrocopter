import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pyrealsense2 as rs

from l515 import L515

def PlotTrajectory3D(dt, alpha, capture_delay):
    lidar_cam = L515()

    # init 3D Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("L515 3D-Trajectory")

    x_data, y_data, z_data = [], [], []
    def_orientation = np.array([0.0, 0.0, 0.0])

    while True:
        # get IMU data
        gyro_3d, accel_3d = lidar_cam.GetIMU()

        # apply sensor fusion (Gyroscope + Accelerometer) to calculate trajectory
        gyro_scaled = gyro_3d * dt
        def_orientation += gyro_scaled
        def_orientation = alpha * (def_orientation + gyro_scaled) + (1 - alpha) * accel_3d

        x_data.append(def_orientation[0])
        y_data.append(def_orientation[1])
        z_data.append(def_orientation[2])

        ax.plot3D(x_data, y_data, z_data, "blue")
        plt.draw()
        plt.pause(capture_delay)

def main():
    PlotTrajectory3D(0.1, 0.98, 0.2)

if __name__ == "__main__":
    main()


