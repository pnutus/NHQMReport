from __future__ import division
import scipy as sp
from nhqm.bases import mom_space as mom
from nhqm.problems import He5
from nhqm.bases.contours import gauss_contour
from nhqm.QM_helpers import energies, absq
from numpy.linalg import norm
from collections import namedtuple
import matplotlib.pyplot as plt


plot = False

problem = He5
k_max = 3
order = 100
num_wfs = 10
QNums = namedtuple('qnums', 'l j')
Q = QNums(l=1, j=1.5)
problem.V0=-50

contour = gauss_contour((0, 0.2 -0.2j, k_max), [order/2,order/2])
points, weights = contour

H = mom.hamiltonian(contour, problem, Q)
eigvals_real, eigvecs_real = energies(H)

contour = gauss_contour((0, k_max), order)
points, weights = contour

H = mom.hamiltonian(contour, problem, Q)
eigvals_comp, eigvecs_comp = energies(H)

rmax = 100
r_order = 500
r = sp.linspace(1e-1, rmax, r_order)

def sqrd_wf(eigvec):
    wf = mom.gen_wavefunction(eigvec, Q, contour)
    return r_order / rmax * r**2 * absq(wf(r))*10/ norm(r*wf(r))**2 

result_real = [r]
result_comp = [r]    
    
for i in xrange(num_wfs):
    real_vec = eigvecs_real[:,i]
    comp_vec = eigvecs_comp[:,i]  
    
    result_real.append(sqrd_wf(real_vec))  
    result_comp.append(sqrd_wf(comp_vec))
    
    lim=0
    mid=53
    if plot and i>= mid -lim and i <= mid+lim:
        plt.plot(momenta, real_vec)
        plt.plot(momenta, comp_vec)
            
realdata = sp.array(result_real).T
compdata = sp.array(result_comp).T

import os
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "wavefunctions_real.data", realdata)
sp.savetxt(script_dir + "wavefunctions_complex.data", compdata)

if plot:
    plt.show()



