from __future__ import division
import scipy as sp
from nhqm.bases import mom_space as mom
from nhqm.problems import He5
from nhqm.bases.gen_contour import gauss_contour
from nhqm.QM_helpers import energies, absq
from numpy.linalg import norm

problem = He5
k_max = 3
order = 100

contour = gauss_contour((0, k_max), order)
ks, _ = contour
Q = mom.QNums(l=1, j=1.5, k=ks)

problem.V0 = -52
H = mom.hamiltonian(contour, problem, Q)
eigvals_1, eigvecs_1 = energies(H)

problem.V0=-50
H = mom.hamiltonian(contour, problem, Q)
eigvals_2, eigvecs_2 = energies(H)

problem.V0=-70
H = mom.hamiltonian(contour, problem, Q)
eigvals_3, eigvecs_3 = energies(H)

rmax = 100
r_order = 500
r = sp.linspace(1e-1, rmax, r_order)

def sqrd_wf(eigvec):
    wf = mom.gen_wavefunction(eigvec, contour, Q)
    return r_order / rmax * r**2 * absq(wf(r))*10/ norm(r*wf(r))**2 

wf1_res = sqrd_wf(eigvecs_1[:,8])
wf1 = sqrd_wf(eigvecs_1[:,17])

wf2_res = sqrd_wf(eigvecs_2[:,13])
wf2 = sqrd_wf(eigvecs_2[:,17])

wavefunctiondata = sp.array([r, wf1_res, wf1, wf2_res, wf2])
import os
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
sp.savetxt(script_dir + "wavefunctions.data", wavefunctiondata.T)

"""
fig1 = plts.plot_init()
fig1.clf()
ax1=fig1.add_subplot(121)
ax2=fig1.add_subplot(122)

ax1.plot(r, wf1_res, 'k')
ax1.plot(r, wf1, 'k', ls='dashed') 

ax2.plot(r, wf2_res, 'k')
ax2.plot(r, wf2, 'k', ls ='dashed') 

ax1.axis([0, 100, 0, 1.6])
ax1.set_xlabel(r'$r$ [fm]')
ax1.set_ylabel(r'$r^2|R(r)|^2$')
fig1.text(0.25, 0.5, r'$V_0 = -52$ MeV')

plts.show_only_bot(ax1)
plts.show_only_bot(ax2)

ax2.axis([0, 100, 0, 1.6])
ax2.set_xlabel(r'$r$ [fm]')
fig1.text(0.7, 0.5, r'$V_0 = -47$ MeV')

plt.savefig('out.pdf', transparent=True, bbox_inches='tight', pad_inches=0.1) 
"""
