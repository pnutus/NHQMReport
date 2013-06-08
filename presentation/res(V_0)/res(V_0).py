from __future__ import division
import scipy as sp
from nhqm.bases import mom_space as mom
from nhqm.problems import He5
from nhqm.QM_helpers import energies
from nhqm.bases.contours import triangle_contour, naive_triangle_contour, gauss_contour
from nhqm.plot_helpers import *
from numpy.linalg import norm
from collections import namedtuple


problem = He5 
order = 10*3
V0max = 70
V0min = 40
problem.Vso = -7.04
QNums = namedtuple('qnums', 'l j')
Q = QNums(l=1, j=1.5)
k_max = 2.5

peak_x = 0.17
peak_y = 0.17

def res_index(eigvecs):
    maxes = map(max, abs(eigvecs.T))
    return maxes.index(min(maxes))

contour = triangle_contour(peak_x, peak_y, k_max, order/3)
points, weights = contour

frames = 500

V0s = sp.linspace(60, 32, frames)

result = sp.empty((order,2*frames))

resonances = sp.empty((frames))

for i, V0 in enumerate(V0s):
    problem.V0 = -V0
    points, weights = contour   
    H = mom.hamiltonian(contour, problem, Q)
    eigvals, eigvecs = energies(H)
    ks = sp.sqrt(2*problem.mass*eigvals).T
    idx = res_index(eigvecs)
    pole = ks[idx]
    if sp.real(pole) < 1e-4:
        ks[idx] = 1j*abs(pole)
    result[:,i*2    ] = sp.real(ks)
    result[:,i*2 + 1] = sp.imag(ks)
    resonances[i] = sp.real(eigvals[idx])

import os
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "contour.data", 
    sp.vstack([sp.real(points), sp.imag(points)]).T)
sp.savetxt(script_dir + "solutions.data", result)
sp.savetxt(script_dir + "potentials.data", sp.vstack([V0s, resonances]))