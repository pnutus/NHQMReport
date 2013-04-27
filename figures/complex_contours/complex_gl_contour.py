from nhqm.calculations import QM as calc
import matplotlib.pyplot as plt
import scipy as sp

order = 50
peak_x = 0.7
peak_y = 0.07
k_max = 2.5



fig = plt.figure()

rect = fig.patch
rect.set_facecolor('white')
    
plt.axes(frameon=False)
plt.axis('off')

def res_index(eigvecs):
    maxes = map(max, abs(eigvecs.T))
    return maxes.index(min(maxes))

contour = calc.triangle_contour(peak_x, peak_y, k_max, order/3)

points, _ = contour
plt.plot(sp.real(points), sp.imag(points), 'o', markersize=4,
markeredgewidth=1,markeredgecolor='k',
markerfacecolor='None')

plt.plot([-0.05, 2.95],[0, 0], color='k')
plt.plot([0, 0],[-0.12, 0.04], color='k')

plt.xlim([-.1,3])
plt.ylim([-.13,.05])

plt.arrow( 2.85, 0, 0.05, 0, fc="k", ec="w",linewidth=1,
head_width=0.0051, head_length=0.06 )

plt.arrow( 0, -0.01,0, 0.05, fc="k", ec="w",linewidth=1,
head_width=0.05, head_length=0.005 )

fig.text(0.16, 0.82, r'Im $k$', fontsize=15)


fig.text(0.83, 0.69, r'Re $k$', fontsize=15)



plt.show()