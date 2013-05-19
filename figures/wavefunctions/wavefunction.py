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
order = 100
std = 26
contour = gauss_contour((0, k_max), order)
ks, _ = contour

QNums = namedtuple('qnums', 'l j k')
Q = QNums(l=1, j=1.5, k=ks)

problem.V0 = -70
H = mom.hamiltonian(contour, problem, Q)
eigvals_1, eigvecs_1 = energies(H)

# problem.V0=-60
# H = mom.hamiltonian(contour, problem, Q)
# eigvals_2, eigvecs_2 = energies(H)

problem.V0=-52
H = mom.hamiltonian(contour, problem, Q)
eigvals_3, eigvecs_3 = energies(H)

problem.V0=-47
H = mom.hamiltonian(contour, problem, Q)
eigvals_4, eigvecs_4 = energies(H)

problem.V0=-40
H = mom.hamiltonian(contour, problem, Q)
eigvals_5, eigvecs_5 = energies(H)

rmax = 100
r_order = 200
r = sp.linspace(1e-1, rmax, r_order)


def sqrd_wf(eigvec):
    wf = mom.gen_wavefunction(eigvec, Q, contour)
    return r_order / rmax * r**2 * absq(wf(r))*10/ norm(r*wf(r))**2 

wf1_res = sqrd_wf(eigvecs_1[:,0])
wf1 = sqrd_wf(eigvecs_1[:,std])
print "-70 'res'", eigvals_1[0] 
print "-70 unbound", eigvals_1[std] 

# wf2_res = sqrd_wf(eigvecs_2[:,0])
# wf2 = sqrd_wf(eigvecs_2[:,std])
# print "-60 'res'", eigvals_2[0] 
# print "-60 unbound", eigvals_2[std] 

wf3_res = sqrd_wf(eigvecs_3[:,8])
wf3 = sqrd_wf(eigvecs_3[:,std])
print "-52 'res'", eigvals_3[8] 
print "-52 unbound", eigvals_3[std] 

wf4_res = sqrd_wf(eigvecs_4[:,16])
wf4 = sqrd_wf(eigvecs_4[:,std])
print "-47 'res'", eigvals_4[16] 
print "-47 unbound", eigvals_4[std] 

wf5_res = sqrd_wf(eigvecs_5[:,21])
wf5 = sqrd_wf(eigvecs_5[:,std])
print "-40 'res'", eigvals_5[16] 
print "-40 unbound", eigvals_5[std] 
# x=20
# a = sqrd_wf(eigvecs_5[:,x])
# b = sqrd_wf(eigvecs_5[:,x+1])
# c = sqrd_wf(eigvecs_5[:,x+2])
# d = sqrd_wf(eigvecs_5[:,x+3])


wavefunctiondata = sp.array([r, wf1_res, wf1, wf3_res, wf3, wf4_res, wf4, wf5_res, wf5])
import os
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "wavefunctions.data", wavefunctiondata.T)

plt.plot(r, wf5_res, 'k')
plt.plot(r, wf5, 'k', ls='dashed')
# 
# plt.plot(r, a, 'r')
# plt.plot(r, b, 'g')
# plt.plot(r, c, 'b')
# plt.plot(r, d, 'r', ls='dashed')
plt.axis([0, rmax, 0, 1.6])
plt.xlabel(r'$r$ [fm]')
plt.ylabel(r'$r^2|R(r)|^2$')
plt.show()

