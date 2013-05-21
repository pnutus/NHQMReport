from __future__ import division
import scipy as sp
import os
from collections import namedtuple
from nhqm.bases import harm_osc as osc, mom_space as mom
from nhqm.problems import H_atom, He5
from nhqm.QM_helpers import energies
from nhqm.bases.contours import gauss_contour
    
mom.integration_order = 60
mom.integration_range = 10
osc.integration_order = 60
osc.integration_range = 20

problem = H_atom
problem.HO_omega = 1

QNums = namedtuple('qnums', 'l j')
Q = QNums(l=0, j=.5)
basis_sizes = range(1,30)
k_max = 10

res_HO = []
res_mom = []


for basis_size in basis_sizes:
    H = osc.hamiltonian(basis_size, problem, Q)
    eigvals, eigvecs = energies(H)
    res_HO.append(eigvals[0]*problem.eV_factor)

    contour = gauss_contour([0, k_max], basis_size)
    H = mom.hamiltonian(contour, problem, Q)
    eigvals, eigvecs = energies(H)
    res_mom.append(eigvals[0]*problem.eV_factor) 
    
    print "h", basis_size
        
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "hydrogen_convergence.data", 
            sp.array([basis_sizes, res_HO, res_mom]).T)
            
            
V0 = -70            
problem = He5 
problem.V0=V0
l = 0
j = 0.5

res_HO_He5 = []
res_mom_He5 = []

for basis_size in basis_sizes:
    H = osc.hamiltonian(basis_size, problem, Q)
    eigvals, eigvecs = energies(H)
    res_HO_He5.append(eigvals[0])

    contour = gauss_contour([0, k_max], basis_size)
    H = mom.hamiltonian(contour, problem, Q)
    eigvals, eigvecs = energies(H)
    res_mom_He5.append(eigvals[0]) 
    
    print "he5", basis_size
        
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "He5_convergence.data", 
            sp.array([basis_sizes, res_HO_He5, res_mom_He5]).T)

            