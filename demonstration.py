import numpy as np
import pptk


# load point cloud
points = np.load("tree.npy")
points = points[:, :3]
colors = np.ones((len(points), 3)) * 255

# initiate viewer
v = pptk.viewer(points)
v.attributes(colors)
v.set(point_size=0.01)
v.set(lookat=np.mean(points, axis=0))
