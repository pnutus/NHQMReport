from __future__ import division

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from nhqm.bases import mom_space as mom
from nhqm.problems import He5
from nhqm.QM_helpers import energies
from nhqm.bases.contours import triangle_contour, gauss_contour
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))


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
    
    
p32res_exp = 0.17 -0.03j

def find_closest(vec, val=p32res_exp):
    #returns index, value
    index= min(range(len(vec)), key=lambda i: abs(vec[i]-val))
    
    """
    TODO:
    Raise a flag or w/e if the closest value is too close
    i e no pole was found
    """
    return index, vec[index]    

problem = He5 
l = 1
j = 1.5
args = (problem, l, j)
k_max=5
order = 60

peak_x = 0.2
peak_y = 0.2

sierp_x = 0.17
sierp_y = -0.1j
sierpa = 0.5*sierp_x
sierpb = 2*sierp_y
sierpc = 0.99*sierp_x + 2*sierp_y
sierpd = 0.51*sierp_x + sierp_y
sierpe = 1.49*sierp_x + sierp_y
sierpf = 1.01*sierp_x + 2*sierp_y
sierpg = 2*sierp_x + 2*sierp_y
sierph = 1.5*sierp_x


sierpinski = gauss_contour([0, sierpa, sierpb,  sierpg, sierph, k_max], [  9,19,39,19,  200])

contours = [triangle_contour(peak_x, peak_y, k_max, order/3), gauss_contour([0, 0 -peak_y*1j, 2*peak_x -peak_y*1j, 2*peak_x, k_max], [order/4,order/4,order/4,order/4])]

V0 = -47
k_res = []

for m, contour in enumerate(contours):
    problem.V0=V0
    k_res.append(sp.empty(len(contour[0]), 'complex'))
    QNums = namedtuple('qnums', 'l j k')
    Q = QNums(l=1, j=1.5, k=len(contour[0]))
    H = mom.hamiltonian(contour, problem, Q)
    eigvals, eigvecs = energies(H)
    
    print res_index(eigvecs)
    
    
    for i in xrange(len(eigvals)):
        k_res[m][i] = sp.sqrt(2*problem.mass*eigvals[i])
        if sp.real(k_res[m][i])<10 ** -6:
            k_res[m][i] = abs(k_res[m][i]) * 1j
        if sp.imag(k_res[m][i]) > 0:
            k_res[m][i] = sp.conj(k_res[m][i])  
            
    print find_closest(k_res[m])
    
    print "::::" 
    
cont0, _ = contours[0] 
cont1, _ = contours[1]
# cont2, _ = contours[2]  

triangle   = sp.array([sp.real(cont0),sp.imag(cont0),sp.real(k_res[0]),sp.imag(k_res[0])])
square     = sp.array([sp.real(cont1),sp.imag(cont1),sp.real(k_res[1]),sp.imag(k_res[1])])
# sierpinski = sp.array([sp.real(cont2),sp.imag(cont2),sp.real(k_res[2]),sp.imag(k_res[2])])

script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"

#sp.savetxt(script_dir + "square.data", square.T)
#sp.savetxt(script_dir + "triangle.data", triangle.T)
# sp.savetxt(script_dir + "sierpinski.data", sierpinski.T)