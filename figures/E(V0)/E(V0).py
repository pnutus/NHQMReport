from __future__ import division
import scipy as sp
import os
from nhqm.bases import harm_osc as osc, mom_space as mom
from nhqm.problems import H_atom, He5
from nhqm.QM_helpers import energies
from nhqm.bases.gen_contour import gauss_contour
import matplotlib.pyplot as plt


order=25
problem = He5
Q = osc.QNums(l=0, j=.5, n=range(order))
order_nr = 40
V0s = sp.linspace(-40, 40, order_nr)
res_mom = []

print len(V0s)

for V0 in V0s:
    print V0
    problem.V0=V0
    contour = gauss_contour([0, 5], order)
    H = mom.hamiltonian(contour, problem, Q)
    eigvals, eigvecs = energies(H)
    res_mom.append(eigvals[0:10]*problem.eV_factor) 
    print "  ", eigvals[0]*problem.eV_factor

plt.plot(V0s,res_mom)
plt.show()
    
    
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "E(V0).data", 
            sp.array([V0s, res_mom]).T)