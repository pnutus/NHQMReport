from __future__ import division
import scipy as sp
from nhqm.bases import mom_space as mom
from nhqm.problems import He5
from nhqm.bases.gen_contour import gauss_contour
from nhqm.QM_helpers import energies, absq
from numpy.linalg import norm
from collections import namedtuple
import matplotlib.pyplot as plt


problem = He5
k_max = 3
order = 100
num_wfs = 30

contour = gauss_contour((0, 0.2 -0.2j, k_max), [order/2,order/2])
points, weights = contour
momenta = sp.absolute(points)

QNums = namedtuple('qnums', 'l j k')
Q = QNums(l=1, j=1.5, k=points)

problem.V0=-50
H = mom.hamiltonian(contour, problem, Q)
eigvals, eigvecs = energies(H)

result_physvec = [momenta]
result_symmvec = [momenta]
def un_symmetrize(eigvec):
    for i in xrange(len(eigvec)):
        eigvec[i] = eigvec[i] / sp.sqrt(weights[i]) / points[i]
    return eigvec   
    
# print eigvecs[:,0]
# print un_symmetrize(eigvecs[:,0])     
    
for i in xrange(num_wfs):   
    temp_vec = eigvecs[:,i]
    symm_vec = sp.absolute(temp_vec)**2  
    result_symmvec.append(symm_vec)  
    
    temp_phys_vec = un_symmetrize(temp_vec)
    phys_vec = sp.absolute(temp_phys_vec)**2
  
    
    result_physvec.append(phys_vec)

    

physdata = sp.array(result_physvec).T
print physdata

symmdata = sp.array(result_symmvec).T
print symmdata

import os
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "physical_eigvecs.data", physdata)
sp.savetxt(script_dir + "symmetric_eigvecs.data", symmdata)

