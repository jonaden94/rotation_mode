from cloud import *
import numpy as np
import json


def explore1(tree_number, points_path, position_path, subsetting, radius, save=False):
    """
    :param save: save chunk
    :param tree_number: number of tree that forms center of plot
    :param points_path: number of points that forms center of plot
    :param datapath: path of data to plot
    :param subsetting: only plot every subsetting-th poínt
    :param  radius: plot radius around selected tree
    :return: None
    """

    with open(position_path, "r") as f:
        centers = json.load(f)

    for i in range(len(centers)):
        if int(centers[i][0]) == tree_number:
            center = centers[i][1]

    # instantiate cloud class
    cloud = Cloud(points_path=points_path, position_path=position_path, subsetting=subsetting)

    # select regional subset of points
    cloud.filter(center, radius=radius, remove999=False)

    if save:
        np.save("../data/numpydata/chunks/filtered_points.npy", cloud.filtered_points)

    # plot
    cloud.plot_pptk()


points_path = "../data/numpydata/forest_labeled_cleanest.npy"
#points_path = "G:/Meine Ablage/Colab/tree_learning/01234/61.npy"
#points_path = "G:/Meine Ablage/Colab/tree_learning/01234/100.npy"
position_path = "../data/numpydata/positions_attempt2.json"
# tree_path = "../data/numpydata/Trees/tree243.npy"

explore1(tree_number=61, points_path=points_path, position_path=position_path, subsetting=15, radius=10)
# explore(tree_number=0, datapath=LearnDataPath, subsetting=15, radius=10)
# explore(tree_number=200, datapath=TreePath, subsetting=15, radius=10)



# points = np.load(points_path)
# targets = points[:, 3]
# points = points[:, :3]
#
# import pptk
#
#
#
# colors = np.ones((len(points), 3)) * targets.reshape(len(targets), 1)
#
#
# v = pptk.viewer(points)
# v.attributes(colors)
# v.set(point_size=0.01)
