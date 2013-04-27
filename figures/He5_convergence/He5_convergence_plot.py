from __future__ import division
#from imports import *

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from nhqm.bases import harm_osc as osc, mom_space as mom
from nhqm.problems import H_atom, He5
from nhqm.QM_helpers import energies
from nhqm.bases.gen_contour import gauss_contour
import plot_setup as pltset
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import He5_convergence_data as data

def lmin(lista):
    minv = lista[0]
    for i in xrange(len(lista)):
        if lista[i] < minv:
            minv = lista[i]
    return minv 
    
def lmax(lista):
    maxv = lista[0]
    for i in xrange(len(lista)):
        if lista[i] > maxv:
            maxv = lista[i]
    return maxv   

mom.integration_order = 20
mom.integration_range = 10
osc.integration_order = 60


#ordermatrix=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [14,16,18,20,22,24,26,28,30,33,36,39,42,45,48,51,55,59,63,67]]
ordermatrix =[[1,2,3,4,5,6,7,8,9,10], [10,15,20,25,30,40,50]]


resho, resm = data.calc(ordermatrix, overwrite=False)


fig = pltset.plot_init(font_size=14,tick_size=11) #set font sizes.


#fixes subplots, and size
gs = gridspec.GridSpec(1,2,
                       width_ratios=[1,2]
                       )
ax2 = plt.subplot(gs[0])
ax3 = plt.subplot(gs[1])
ax_list = [ax2, ax3]


ax2.set_ylabel('Energy [MeV]')
plot_title=plt.title('Convergence of the He5 resonance for HO, mom')
#ad hoc solutions to title position
plot_title.set_y(1.03)
plot_title.set_x(0.13)


for i, orderlist in enumerate(ordermatrix):
    ax = ax_list[i]
    l1, l2 = ax.plot(orderlist, resho[i], 'kD-', orderlist, resm[i], 'ks-', markersize=7,
markeredgewidth=1,markeredgecolor='k',
markerfacecolor='None')
    ax.set_xlabel('order')
        
ax_list[1].set_ylim([-24.93, -24.92])
ax_list[1].get_xaxis().get_major_formatter().set_useOffset(False)
#ax_list[1].set_xlim([lmin(ordermatrix[1]), lmax(ordermatrix[1])])

ax_list[1].set_autoscale_on(False)
ax_list[1].legend( (l1, l2),
        ('Harmonic Oscillator', 'Momentun Space'),
        'lower right')
        
pltset.remove_top_right(ax2)  
pltset.remove_top_right(ax3)        
    
plt.show() 