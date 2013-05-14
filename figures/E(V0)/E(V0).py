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

basis_size=10
problem = He5
num_V0 = 20
QNums = namedtuple('qnums', 'l j J M E m')
Q = QNums(l=1, j=1.5, J=0, M=0, 
          m=[-1.5, -0.5, 0.5, 1.5],
          E=range(num_V0))
V0s = sp.linspace(-65, -40, num_V0)
res_mom = []

print len(V0s)

for V0 in V0s:
    print V0
    problem.V0=V0
    contour = gauss_contour([0, 5], basis_size)
    H = mom.hamiltonian(contour, problem, Q)
    eigvals, eigvecs = energies(H)
    res_mom.append(eigvals[0:10])
    # print "  ", eigvals[0:3]

plt.plot(V0s,res_mom)
plt.show()

# print zip(*res_mom)
# print [V0s]

script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "E(V0).data", 
            sp.array([V0s]+zip(*res_mom)).T)