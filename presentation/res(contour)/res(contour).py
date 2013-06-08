from __future__ import division
import scipy as sp
from nhqm.bases import mom_space as mom
from nhqm.problems import He5
from nhqm.QM_helpers import energies
from nhqm.bases.contours import triangle_contour, naive_triangle_contour, gauss_contour
from nhqm.plot_helpers import *
from numpy.linalg import norm
from collections import namedtuple


fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111)
ax.axis([-0.02, 0.7, -0.11, 0.01])


problem = He5 
order = 10*3
problem.V0 = -47.05
problem.Vso = -7.04
QNums = namedtuple('qnums', 'l j J M E m')
Q = QNums(l=1, j=1.5, J=0, M=0, 
          m=[-1.5, -0.5, 0.5, 1.5], 
          E=range(order))
k_max = 2.5

peak_x = 0.17

frames = 500

peak_ys = sp.linspace(0, 0.1, frames)

result = sp.empty((order,4*frames))

for i, peak_y in enumerate(peak_ys):
    contour = triangle_contour(peak_x, peak_y, k_max, order/3)
    points, weights = contour
    H = mom.hamiltonian(contour, problem, Q)
    eigvals, eigvecs = energies(H)
    ks = sp.sqrt(2*problem.mass*eigvals)
    result[:,i*4    ] = sp.real(points).T
    result[:,i*4 + 1] = sp.imag(points).T
    result[:,i*4 + 2] = sp.real(ks).T
    result[:,i*4 + 3] = sp.imag(ks).T

import os
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "res(contour).data", result)