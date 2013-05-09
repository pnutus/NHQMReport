from __future__ import division

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from nhqm.bases import mom_space as mom
from nhqm.problems import He5
from nhqm.QM_helpers import energies
from nhqm.bases.gen_contour import triangle_contour
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
import plot_setup as plts

import matplotlib.pyplot as plt

import scipy as sp
import timeit

def res_index(eigvecs):
    maxes = map(max, abs(eigvecs.T))
    return maxes.index(min(maxes))

def absq(x):
    return x*sp.conjugate(x)

def logspace(min, max, order):
    return sp.around(sp.logspace(log(min), log(max), order))

problem = He5 
l = 1
j = 1.5
args = (problem, l, j)
k_max=5
order = 30

peak_x = 0.2
peak_y = 0.2
order_nr = 5
V0s = sp.linspace(-65, -40, order_nr)

rmax=40
r = sp.linspace(1e-1, rmax, 2000)

fig = plts.plot_init()

plt.xlabel(r'Re $k$')
plt.ylabel(r'Im $k$')

ax = fig.add_subplot(1,1,1)
plts.center_axis(ax)

k_res=sp.empty(order_nr, 'complex')

for m, V0 in enumerate(V0s):
    problem.V0=V0
    print order_nr-m, 'to go'
    contour = triangle_contour(peak_x, peak_y, k_max, order/3)
    ks, _ = contour
    Q = mom.QNums(l=1, j=1.5, k=range(len(contour[0])))
    H = mom.hamiltonian(contour, problem, Q)
    eigvals, eigvecs = energies(H)
    res = res_index(eigvecs)
    k_res[m]=sp.sqrt(2*problem.mass*eigvals[res])
    if sp.real(k_res[m])<10 ** -6:
        k_res[m] = abs(k_res[m]) * 1j
    #eigvecs_res[:,m] = eigvecs[:,res]
    #reswf = calc.gen_wavefunction(eigvecs[:,res], basis_function, contour)
    #reswf = calc.normalize(reswf, 0, 20, weight= lambda r: r**2)
    #absq_wavefunctions_res[:,m] = r**2 * absq(reswf(r))
print 'done'
ax.plot(sp.real(k_res), sp.imag(k_res), 'kD', markersize=7,
markeredgewidth=1,markeredgecolor='k',
markerfacecolor='None')

plts.plot_contour(contour,ax)
plt.xlim([-0.05,3])

k=sp.sqrt(2*problem.mass*eigvals)
#plt.plot(sp.real(k), sp.imag(k), 'kd-', markersize=5,
#markeredgewidth=1,markeredgecolor='k',
#markerfacecolor='None')
#plt.plot(sp.real(ks), sp.imag(ks), 'ro', markersize=3)

#plt.figure(1)
#plt.plot(r, absq_wavefunctions_res[:,0])


plt.show()
