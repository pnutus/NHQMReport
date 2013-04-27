import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import matplotlib
import scipy as sp


matplotlib.rc('xtick', color='white')
matplotlib.rc('ytick', color='white')

def dual_half_circle(center, radius, angle=0, ax=None,
                     **kwargs):
    """
    Add two half circles to the axes *ax* (or the current axes) with the 
    specified facecolors *colors* rotated at *angle* (in degrees).
    """
    if ax is None:
        ax = plt.gca()
    theta1, theta2 = angle, angle + 180
    w1 = Wedge(center, radius, theta1, theta2, fc='b', **kwargs)
    ax.add_artist(w1)
    return w1
    
fig, ax = plt.subplots()
dual_half_circle((0.5,0.5), radius=0.4, angle=0, ax=ax)
ax.axis('equal')

fig.set_figheight(6)
fig.set_figwidth(6)

rect = fig.patch
rect.set_facecolor('white')
    
plt.axes(frameon=False)




#axes
plt.plot([0.05, 0.95],[0.5, 0.5], color='k')
plt.plot([0.5, 0.5],[0.05, 0.95], color='k')

#triangle 4th
plt.plot([0.5, 0.65],[0.5, 0.4], color='k', linewidth=2)
plt.plot([0.65, 0.8],[0.4, 0.5], color='k', linewidth=2)

#triangle 3rd
plt.plot([0.35, 0.5],[0.6, 0.5], color='k', linewidth=2)
plt.plot([0.2, 0.35],[0.5, 0.6], color='k', linewidth=2)

#extra emphassis
plt.plot([0.1, 0.2],[0.5, 0.5], color='k', linewidth=2)
plt.plot([0.8, 0.9],[0.5, 0.5], color='k', linewidth=2)

plt.xlim([0,1])
plt.ylim([0,1])


plt.plot([0.5, 0.5],[0.65, 0.58], "o", markersize=7,
markeredgewidth=1,markeredgecolor='k',
markerfacecolor='None'
)
plt.plot([0.65, 0.35],[0.45, 0.55], 'x')

r = 0.4
x1 = sp.linspace(0, 0.4, 200)
x2 = sp.linspace(0.4, 0, 200)
y1 =[]
y2= []
for i in xrange(len(x1)):
    y1.append(0.5 + sp.sqrt(r**2 - x1[i]**2))
    x1[i]+= 0.5
    y2.append(0.5 + sp.sqrt(r**2 - ( r-x2[i])**2))
    x2[i] +=0.1

plt.plot(x1,y1, color='k', linewidth=2)
plt.plot(x2,y2, color='k', linewidth=2)

plt.show()