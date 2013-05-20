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
a=0.5
b=10
r0list=sp.linspace(a,b,500)
omegalist=[]
for r in r0list:
    omegalist.append(1/(problem.mass*r*r))
basis_size=100
k_max=3

contour = gauss_contour([0, k_max], basis_size)
points, _ = contour
QNums = namedtuple('qnums', 'l j J M E m')
Q = QNums(l=1, j=1.5, J=0, M=0, 
          m=[-1.5, -0.5, 0.5, 1.5],
          E=range(basis_size))

res_osc = []

trunc_at = 5
trunc_val = 5

for i,omega in enumerate(omegalist):
    print (i+1),":",omega
    problem.HO_omega=omega
    H = osc.hamiltonian(basis_size, problem, Q)
    eigvals, _ = energies(H)
    res_osc.append(eigvals[0:20])

for ev in res_osc:
    for e in ev:
        if e > trunc_at:
            e = trunc_val
    
print "done"

# range = []
# for om in omegalist:
    # range.append(1/sp.sqrt(problem.mass*om))

# plt.plot(r0list,res_osc)
# plt.show()

script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "E(omega).data", 
            sp.array([r0list]+zip(*res_osc)).T)