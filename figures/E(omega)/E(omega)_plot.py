from __future__ import division
import scipy as sp
import os
from nhqm.problems import H_atom, He5
import matplotlib.pyplot as plt
from collections import namedtuple
from nhqm.QM_helpers import energies, symmetric, hermitian
from nhqm.bases.gen_contour import triangle_contour, gauss_contour
from nhqm.bases import (mom_space            as mom, 
                        harm_osc             as osc, 
                        mb_coupled           as coupled, 
                        mb_uncoupled         as uncoupled,
                        two_body_interaction as n_n)
from nhqm.plot_helpers import *

problem = He5
osc.integration_order = 30
problem.V0 = -52
a=0
b=50
omegalist= sp.linspace(a,b,6)
basis_size=50
k_max=3

contour = gauss_contour([0, k_max], basis_size)
points, _ = contour
QNums = namedtuple('qnums', 'l j J M E m')
Q = QNums(l=1, j=1.5, J=0, M=0, 
          m=[-1.5, -0.5, 0.5, 1.5],
          E=range(basis_size))

res_osc=[]

for omega in omegalist:
    print omega
    problem.HO_omega=omega
    H = osc.hamiltonian(basis_size, problem, Q)
    eigvals, _ = energies(H)
    res_osc.append(eigvals[0:10])

print "done"

plt.plot(omegalist,res_osc)
plt.show()

script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "E(omega).data", 
            sp.array([omegalist]+zip(*res_osc)).T)