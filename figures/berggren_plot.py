import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np

def dual_half_circle(center, radius, angle=0, ax=None,
                     **kwargs):
    """
    Add two half circles to the axes *ax* (or the current axes) with the 
    specified facecolors *colors* rotated at *angle* (in degrees).
    """
    if ax is None:
        ax = plt.gca()
    theta1, theta2 = angle, angle + 180
    w1 = Wedge(center, radius, theta1, theta2, fc='w', **kwargs)
    ax.add_artist(w1)
    return w1

def plot_axis(ax=None):
    if ax is None:
        ax = plt.gca()
    l1 = vlines(0.5, 0.1, 0.9, color='k', linestyles='solid')
    ax.add_artist(l1)
    return l1
    
fig, ax = plt.subplots()
dual_half_circle((0.5,0.5), radius=0.4, angle=0, ax=ax)
plot_axis
ax.axis('equal')


l = plt.axvline(x=0.5, ymin=0.05, ymax=0.95, linewidth=1, color='k')
l = plt.axhline(y=.5, xmin=0.05, xmax=0.95, color='k')
plt.xlim([0,1])

ax_list[1].autoscale_on(False)



plt.show()