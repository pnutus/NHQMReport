from nhqm.bases.gen_contour import triangle_contour
import matplotlib
import matplotlib.pyplot as plt
import scipy as sp

order = 50
peak_x = 0.5
peak_y = 0.5
k_max = 1.8

matplotlib.rc('text', usetex=False )
matplotlib.rc('font', family='serif')
matplotlib.rcParams['text.latex.unicode']=True

fig = plt.figure()


plt.axis('off')
plt.axis('equal')

contour = triangle_contour(peak_x, peak_y, k_max, order/3)

points, _ = contour
plt.plot(sp.real(points), sp.imag(points), 'o', markersize=4,
markeredgewidth=1,markeredgecolor='k',
markerfacecolor='None')


plt.xlim([-.1,2])
plt.ylim([-.6,.3])

plt.arrow( -0.05, 0, 2, 0, color="k", 
            length_includes_head=True, head_width = 0.03)
plt.arrow( 0, -0.6, 0, 1,  color="k", 
            length_includes_head=True, head_width = 0.03)

fig.text(0.16, 0.78, r'Im $k$', fontsize=15)
fig.text(0.83, 0.6, r'Re $k$', fontsize=15)

plt.savefig('complex_contour.pdf', transparent=True, bbox_inches='tight', pad_inches=0)