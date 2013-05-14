from __future__ import division

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from nhqm.bases import mom_space as mom
from nhqm.problems import He5
from nhqm.QM_helpers import energies
from nhqm.bases.gen_contour import triangle_contour, gauss_contour
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
import plot_setup as plts

import matplotlib.pyplot as plt
from collections import namedtuple


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
order = 60

peak_x = 0.2
peak_y = 0.2
contour=gauss_contour([0, k_max], order)

V0s = [-70,-50]
k_res = sp.empty((len(V0s), order), 'complex')

for m, V0 in enumerate(V0s):
    problem.V0=V0

    QNums = namedtuple('qnums', 'l j k')
    Q = QNums(l=1, j=1.5, k=len(contour))
    H = mom.hamiltonian(contour, problem, Q)
    eigvals, eigvecs = energies(H)
    
    
    for i in xrange(len(eigvals)):
        k_res[m,i] = sp.sqrt(2*problem.mass*eigvals[i])
        if sp.real(k_res[m,i])<10 ** -6:
            k_res[m,i] = abs(k_res[m,i]) * 1j  

pole0r = sp.real(k_res[0])
pole0i = sp.imag(k_res[0])
pole1r = sp.real(k_res[1])
pole1i = sp.imag(k_res[1]) 
res_pole    = sp.array([pole0r, pole0i, pole1r, pole1i])
points, _ = contour
contour_array     = sp.array([sp.real(points), sp.imag(points)])

script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"

sp.savetxt(script_dir + "poles.data", res_pole.T)
sp.savetxt(script_dir + "contour.data", contour_array.T)
