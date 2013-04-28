from __future__ import division

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

#from imports import *
from nhqm.bases import harm_osc as osc, mom_space as mom
from nhqm.problems import H_atom, He5
from nhqm.QM_helpers import energies
from nhqm.bases.gen_contour import gauss_contour
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
import plot_setup as plts
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import hydrogen_convergence_data as data

mom.integration_order = 20
mom.integration_range = 10
osc.integration_order = 60

"""
TODO

change xlable from order to Number of Basis Size N """


ordermatrix=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [14,16,18,20,22,24,26,28,30,33,36,39,42,45,48,51,55,59,63,67]]



resho, resm = data.calc(ordermatrix, overwrite=False)


fig = plts.plot_init(font_size=14,tick_size=11) #set font sizes.

#fixes subplots, and size
gs = gridspec.GridSpec(1,2,
                       width_ratios=[1,2]
                       )
ax2 = plt.subplot(gs[0])
ax3 = plt.subplot(gs[1])
ax_list = [ax2, ax3]


ax2.set_ylabel('energy [Hartree]')
plot_title=plt.title('Convergence of the Hydrogen groundstate for HO, mom')
#ad hoc solutions to title position
plot_title.set_y(1.03)
plot_title.set_x(0.13)


for i, orderlist in enumerate(ordermatrix):
    ax = ax_list[i]

    l1, l2 = ax.plot(orderlist, resho[i], 'kD-', orderlist, resm[i], 'ks-', markersize=7,
markeredgewidth=1,markeredgecolor='k',
markerfacecolor='None')
    ax.set_xlabel('order')
    
    if i==1:
        l3 = ax.axhline(y=-0.5, color='r', ls='--')
        
ax_list[1].set_ylim([-0.505, -0.485])

ax_list[1].set_autoscale_on(False)
ax_list[1].legend( (l1, l2, l3),
        ('Harmonic Oscillator', 'Momentum Space', 'Theoretical ground state energy'),
        'lower right')
    
#plt.show() 
plts.save(None, 'hydrogen_convergence2')