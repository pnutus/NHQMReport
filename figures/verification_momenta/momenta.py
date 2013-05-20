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
order=15
contour = gauss_contour((0, 0.2 -0.1j,0.4, 2.5), [order/3,order/3,order/3])
momenta, _ = contour

QNums = namedtuple('qnums', 'l j k')
Q = QNums(l=1, j=1.5, k=momenta)

problem.V0 = -47
H = mom.hamiltonian(contour, problem, Q)
eigvals, eigvecs = energies(H)

def momentum_res(energy):
    return sp.sqrt(2 * problem.mass * energy)

rmax = 100
r_order = 200
r = sp.linspace(1e-1, rmax, r_order)

def sqrd_wf(eigvec):
    wf = mom.gen_wavefunction(eigvec, Q, contour)
    return r_order / rmax * r**2 * absq(wf(r))*10/ norm(r*wf(r))**2 

result =[]
for i in xrange(len(eigvecs)):
    result.append(momentum_res(eigvals[i]))


    
data = sp.array([sp.real(momenta),sp.imag(momenta), sp.real(result), sp.imag(result)])
import os
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "momentum_solutions.data", data.T)

plt.plot(sp.real(momenta),sp.imag(momenta))
plt.plot( sp.real(result), sp.imag(result))
plt.show()


