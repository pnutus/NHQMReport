from __future__ import division

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from nhqm.bases import mom_space as mom
from nhqm.problems import He5
from nhqm.QM_helpers import energies
from nhqm.bases.contours import triangle_contour
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from collections import namedtuple


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
order = 50

peak_x = 0.2
peak_y = 0.2
contour = triangle_contour(peak_x, peak_y, k_max, order/3)
ks, _ = contour


order_nr = 50

QNums = namedtuple('qnums', 'l j k')
Q = QNums(l=1, j=1.5, k=range(len(contour[0])))
    
V0s = sp.linspace(-65, -40, order_nr)
k_res = sp.empty(order_nr, 'complex')

for m, V0 in enumerate(V0s):
    problem.V0=V0
    print order_nr-m, 'to go'

    H = mom.hamiltonian(contour, problem, Q)
    eigvals, eigvecs = energies(H)
    res = res_index(eigvecs)
    k_res[m]=sp.sqrt(2*problem.mass*eigvals[res])
    if sp.real(k_res[m])<10 ** -6:
        k_res[m] = abs(k_res[m]) * 1j
    
res_pole    = sp.array([sp.real(k_res), sp.imag(k_res),V0s])
contour     = sp.array([sp.real(ks), sp.imag(ks)])

script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"

sp.savetxt(script_dir + "poles.data", res_pole.T)
sp.savetxt(script_dir + "contour.data", contour.T)
