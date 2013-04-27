from __future__ import division
#from imports import *
from nhqm.bases import mom_space as mom
from nhqm.bases import many_body as mb
from nhqm.problems import He5
from nhqm.bases.gen_contour import triangle_contour, naive_triangle_contour, gauss_contour
from nhqm.QM_helpers import energies, absq, normalize
from numpy.linalg import norm
import plot_setup as splt
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams['text.usetex']=True
matplotlib.rcParams['text.latex.unicode']=True

splt.plot_init()

problem = He5
k_max = 3
order = 25

peak_x = 0
peak_y = 0
contour = gauss_contour((0, k_max), order)
#contour = naive_triangle_contour(peak_x, peak_y, k_max, order)
ks, _ = contour
Q = mom.QNums(l=1, j=1.5, k=ks)

problem.V0 = -52
H = mom.hamiltonian(contour, problem, Q)
eigvals_1, eigvecs_1 = energies(H)

problem.V0=-50
H = mom.hamiltonian(contour, problem, Q)
eigvals_2, eigvecs_2 = energies(H)

rmax = 100
r_order = 500
r = sp.linspace(1e-1, rmax, r_order)

def sqrd_wf(eigvec):
    wf = mom.gen_wavefunction(eigvec, contour, Q)
    return r_order / rmax * r**2 * absq(wf(r))*10/ norm(r*wf(r))**2 

def plotwf(eigvec, energy, color='k'):
    wf = sqrd_wf(eigvec)
    plt.plot((0, rmax), (energy, energy),'r',linewidth=2)
    plt.plot(r, wf + energy, color, linewidth=3)

wf1_res = sqrd_wf(eigvecs_1[:,8])
wf1_1 = sqrd_wf(eigvecs_1[:,17])

wf2_res = sqrd_wf(eigvecs_2[:,13])
wf2_1 = sqrd_wf(eigvecs_2[:,17])


ax1=plt.subplot(121)
ax2=plt.subplot(122)

ax1.plot(r, wf1_res, 'k', linewidth=2)
ax1.plot(r, wf1_1, 'k', linewidth=2) 

ax2.plot(r, wf2_res, 'k', linewidth=2)
ax2.plot(r, wf2_1, 'k', linewidth=2) 



ax1.axis([0, 100, 0, 1.6])
#ax1.set_xlabel('$r$ [fm]')
ax1.set_ylabel('hej $r^2|R(r)|^2$')
#ax1.set_title('$V0 = -52$')

ax2.axis([0, 100, 0, 1.6])
#ax2.set_xlabel('$r$ [fm]')
#ax2.set_ylabel('$r^2|R(r)|^2$')
#ax2.set_title('lite text $V0 = -47$')

plt.show()

