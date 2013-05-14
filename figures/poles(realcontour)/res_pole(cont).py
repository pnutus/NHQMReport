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

contour = gauss_contour([0, k_max], order)

V0 = -70
k_res = sp.empty( order, 'complex')


problem.V0=V0

QNums = namedtuple('qnums', 'l j k')
Q = QNums(l=1, j=1.5, k=len(contour[0]))
H = mom.hamiltonian(contour, problem, Q)
eigvals, eigvecs = energies(H)
    
    
for i in xrange(len(eigvals)):
    k_res[i] = sp.sqrt(2*problem.mass*eigvals[i])
    if sp.real(k_res[i])<10 ** -6:
        k_res[i] = abs(k_res[i]) * 1j  
    
cont0, _ = contour   
pole0r = sp.real(k_res)
pole0i = sp.imag(k_res) 
res_pole    = sp.array([pole0r, pole0i])
contour_array     = sp.array([sp.real(cont0), sp.imag(cont0)])

script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"

sp.savetxt(script_dir + "poles.data", res_pole.T)
sp.savetxt(script_dir + "contour.data", contour_array.T)
