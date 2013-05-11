from __future__ import division
import scipy as sp
import os
from nhqm.bases import harm_osc as osc, mom_space as mom
from nhqm.problems import H_atom, He5
from nhqm.QM_helpers import energies
from nhqm.bases.gen_contour import gauss_contour



    
mom.integration_order = 20
mom.integration_range = 10
osc.integration_order = 60

problem = He5
problem.HO_omega = 1

orders = range(11,20)
res_HO = []
res_mom = []

for order in orders:

    Q = osc.QNums(l=0, j=.5, n=range(order))
    
    H = osc.hamiltonian(order, problem, Q)
    eigvals, eigvecs = energies(H)
    res_HO.append(eigvals[0]*problem.eV_factor)

    contour = gauss_contour([0, 5], order)
    H = mom.hamiltonian(contour, problem, Q)
    eigvals, eigvecs = energies(H)
    res_mom.append(eigvals[0]*problem.eV_factor) 
        
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "He5_convergence.data", 
            sp.array([orders, res_HO, res_mom]).T)
            