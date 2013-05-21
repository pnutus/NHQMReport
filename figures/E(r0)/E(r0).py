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
problem.V0 = -47
a=0.1
b=2
c=10
r0list=sp.hstack([sp.linspace(a,b,100),sp.linspace(b,c,100)])
omegalist=[]
for r in r0list:
    omegalist.append(1/(problem.mass*r**2))
basis_size=50
k_max=3

contour = gauss_contour([0, k_max], basis_size)
points, _ = contour
QNums = namedtuple('qnums', 'l j')
Q = QNums(l=1, j=1.5)

res_osc = []

truncation = 5

for i,omega in enumerate(omegalist):
    print (i+1),":",omega
    problem.HO_omega=omega
    H = osc.hamiltonian(basis_size, problem, Q)
    eigvals, _ = energies(H)
    res_osc.append(eigvals[0:20])

clipped_res = sp.clip(res_osc, -sp.inf, truncation)

# plt.plot(r0list,clipped_res,'.')
# plt.show()

script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "E(r0).data", 
            sp.array([r0list]+zip(*clipped_res)).T)