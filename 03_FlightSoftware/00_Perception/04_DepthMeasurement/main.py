import matplotlib.pyplot as plt
import numpy as np

from l515 import L515

def main():
    lidar_cam = L515(640, 480)

    fig, ax = plt.subplots()
    depth_map, _ = lidar_cam.GetDepth16()

    img = ax.imshow(depth_map, cmap='jet', vmin=depth_map.max(), vmax=depth_map.min())
    cbar = fig.colorbar(img)
    cbar.set_label('Depth (m)')

    while True:
        depth_map, meas_dist = lidar_cam.GetDepth16()

        img.set_data(depth_map)
        ax.set_title(f"Depth at DMP = {np.round(meas_dist, 2)} m")
        img.set_clim(vmin=depth_map.max(), vmax=depth_map.min())
        
        plt.pause(0.05)

        if plt.waitforbuttonpress(0.05):
            break

if __name__ == "__main__":
    main()
