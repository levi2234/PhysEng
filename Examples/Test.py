from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


def heart_3d(x,y,z):
   return (x**2+(9/4)*y**2+z**2-1)**3-x**2*z**3-(9/80)*y**2*z**3
def plot_implicit(fn, bbox=(-1.5, 1.5)):
    ''' create a plot of an implicit function
    fn  ...implicit function (plot where fn==0)
    bbox ..the x,y,and z limits of plotted interval'''
    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    A = np.linspace(xmin, xmax, 30) # resolution of the contour
    B = np.linspace(xmin, xmax, 10) # number of slices
    A1, A2 = np.meshgrid(A, A) # grid on which the contour is plotted

    coordinates = [] # list to save the coordinates

    for z in B: # plot contours in the XY plane
        X, Y = A1, A2
        Z = fn(X, Y, z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z', colors=('r',))
        # [z] defines the only level to plot for this contour for this value of z
        for seg in cset.allsegs[0]:
            coordinates.extend([(x, y, z) for x, y in zip(seg[:, 0], seg[:, 1])])

    for y in B:  # plot contours in the XZ plane
        X, Z = A1, A2
        Y = fn(X, y, Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y', colors=('red',))
        for seg in cset.allsegs[0]:
                coordinates.extend([(x, y, z) for z, x in zip(seg[:, 0], seg[:, 1])])

    for x in B: # plot contours in the YZ plane
        Y, Z = A1, A2
        X = fn(x, Y, Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x',colors=('red',))
        for seg in cset.allsegs[0]:
            coordinates.extend([(x, y, z) for y, z in zip(seg[:, 0], seg[:, 1])])

    return np.array(coordinates)

if __name__ == '__main__':

    points = plot_implicit(heart_3d)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.scatter(points[:,0], points[:,1], points[:,2], c='r', marker='o')
    plt.show()

    