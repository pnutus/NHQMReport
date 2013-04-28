import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import matplotlib
import scipy as sp


matplotlib.rc('xtick', color='white')
matplotlib.rc('ytick', color='white')

matplotlib.rc('text', usetex=True )
matplotlib.rc('font', family='serif')
matplotlib.rcParams['text.latex.unicode']=True
    
fig, ax = plt.subplots()

ax.axis('equal')

fig.set_figheight(4)
fig.set_figwidth(6)

rect = fig.patch
rect.set_facecolor('white')
    
plt.axes(frameon=False)

"""
TODO:

fix latex regular type fontsize

fix arrow rotation

"""


#axes
plt.plot([0.05, 0.95],[0.5, 0.5], color='k')
plt.plot([0.5, 0.5],[0.35, 0.95], color='k')

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
plt.ylim([0.33,1])

# P.arrow( x, y, dx, dy, **kwargs )
plt.arrow( 0.8, 0.5, 0.05, 0, fc="k", ec="w",linewidth=1,
head_width=0.03, head_length=0.02 )

plt.arrow( 0.1, 0.5, 0.05, 0, fc="k", ec="w",linewidth=1,
head_width=0.03, head_length=0.02 )

plt.arrow( 0.89, 0.5, 0.05, 0, fc="k", ec="w",linewidth=1,
head_width=0.02, head_length=0.02 )

plt.arrow( 0.5, 0.89, 0, 0.05, fc="k", ec="w",linewidth=1,
head_width=0.02, head_length=0.02 )

plt.arrow( 0.753, 0.753, 0.05, 0, fc="k", ec="w",linewidth=1,
head_width=0.03, head_length=0.02 )

plt.arrow( 0.134, 0.753, 0.05, 0, fc="k", ec="w",linewidth=1,
head_width=0.03, head_length=0.02 )

fig.text(0.52, 0.81, r'Im $k$', fontsize=15)


fig.text(0.83, 0.32, r'Re $k$', fontsize=15)

#bound states, resonances

plt.plot([0.5, 0.5],[0.65, 0.58], "o", markersize=7,
markeredgewidth=1,markeredgecolor='k',
markerfacecolor='None'
)
plt.plot([0.65, 0.35],[0.45, 0.55], 'kx')

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
