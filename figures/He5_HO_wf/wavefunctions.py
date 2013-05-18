from __future__ import division
import scipy as sp
from nhqm.bases import harm_osc as osc
from nhqm.problems import He5
from nhqm.bases.gen_contour import gauss_contour
from nhqm.QM_helpers import energies, absq
from numpy.linalg import norm
from collections import namedtuple
import matplotlib.pyplot as plt


problem = He5
k_max = 3
order =50

contour = gauss_contour((0, k_max), order)
ks, _ = contour

QNums = namedtuple('qnums', 'l j k')
Q = QNums(l=1, j=1.5, k=ks)

problem.V0 = -52
H = osc.hamiltonian(order, problem, Q)
eigvals_1, eigvecs_1 = energies(H)

problem.V0=-50
H = osc.hamiltonian(order, problem, Q)
eigvals_2, eigvecs_2 = energies(H)

problem.V0=-70
H = osc.hamiltonian(order, problem, Q)
eigvals_3, eigvecs_3 = energies(H)

rmax = 100
r_order = 500
r = sp.linspace(1e-1, rmax, r_order)

def sqrd_wf(eigvec):
    wf = osc.gen_wavefunction(eigvec, Q, problem, contour)
    return r_order / rmax * r**2 * absq(wf(r))*10/ norm(r*wf(r))**2 

wf1_res = sqrd_wf(eigvecs_1[:,0])
wf1 = sqrd_wf(eigvecs_1[:,17])

wf2_res = sqrd_wf(eigvecs_2[:,13])
wf2 = sqrd_wf(eigvecs_2[:,4])
print "-70", eigvals_3[0]
print "-52", eigvals_2[13]
print "-50", eigvals_1[8]
print "-70", eigvals_3[17]
print "-52", eigvals_2[17]
print "-50", eigvals_1[17]
wf3_res = sqrd_wf(eigvecs_3[:,0])
wf3 = sqrd_wf(eigvecs_3[:,17])

wavefunctiondata = sp.array([r, wf1_res, wf1, wf2_res, wf2, wf3_res, wf3])
import os
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "wavefunctions.data", wavefunctiondata.T)


plt.plot(r, wf1_res, 'k')
plt.plot(r, wf3_res, 'k', ls='dashed') 
#plt.plot(r, wf3, 'r') 
plt.plot(r, wf2, 'r', ls='dashed') 
plt.axis([0, 1.5*rmax, 0, 4.6])
plt.xlabel(r'$r$ [fm]')
plt.ylabel(r'$r^2|R(r)|^2$')

# for i in xrange(5):
#     wf = sqrd_wf(eigvecs_1[:,i])
#     plt.plot(wf)

plt.show()
#plt.savefig('out.pdf', transparent=True, bbox_inches='tight', pad_inches=0.1) 

