from __future__ import division
import scipy as sp
from nhqm.bases import mom_space as mom
from nhqm.problems import He5
from nhqm.bases.contours import gauss_contour
from nhqm.QM_helpers import energies, absq
from numpy.linalg import norm
from collections import namedtuple
import matplotlib.pyplot as plt


problem = He5
k_max = 3
order = 60
num_wfs = order
QNums = namedtuple('qnums', 'l j')
Q = QNums(l=1, j=1.5)
problem.V0=-50

def res_index(eigvecs):
    maxes = map(max, abs(eigvecs.T))
    return maxes.index(min(maxes))

def un_weight(eigvec):
    eigvec_prim = eigvec / sp.sqrt(weights)
    return eigvec_prim / norm(eigvec_prim)


def un_point(eigvec):
    eigvec_prim = eigvec / points
    return eigvec_prim / norm(eigvec_prim)    


def un_symm(eigvec):
    eigvec_prim =  eigvec / sp.sqrt(weights) / points
    return eigvec_prim / norm(eigvec_prim)

contours = [gauss_contour((0, 0.2 -0.2j, 0.4,  k_max), [order/6, order/6, order*2/3]), \
                        gauss_contour((0, k_max), order)]
data = []                        
for j,contour in enumerate(contours):

    points, weights = contour
    momenta = sp.real(points)

    H = mom.hamiltonian(contour, problem, Q)
    eigvals, eigvecs = energies(H)
    result = [momenta]
    
    print "res:", res_index(eigvecs), "beware of off-by-one"

    for i in xrange(num_wfs):
        
        temp_vec = eigvecs[:,i]
        result_vec = sp.absolute(un_weight(temp_vec))**2   
        result.append(result_vec)      
        
    data.append( sp.array(result).T )


import os

script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "eigvecs_real.data", data[1])
sp.savetxt(script_dir + "eigvecs_complex.data", data[0] )



