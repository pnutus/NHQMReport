from __future__ import division
#from imports import *

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from nhqm.bases import harm_osc as osc, mom_space as mom
from nhqm.problems import H_atom, He5
from nhqm.QM_helpers import energies
from nhqm.bases.gen_contour import gauss_contour
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
import plot_setup as plts
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import scipy as sp
import He5_HO_omega_convergence_data as data

osc.integration_order = 30
He5.V0 = -52

#omegalist =[1,2,3,4,5,6,7,8,9,10]
a=0
b=50
omegalist= sp.linspace(a,b,70)

num_energies=10
resho_mat, res_ind = data.calc(omegalist, num_energies, order=20, overwrite=True)
resho_mat_trans = zip(*resho_mat)


fig = plts.plot_init(font_size=14,tick_size=11) #set font sizes.



plt.ylabel('energy [MeV]')
plt.xlabel('omega')
#plot_title=plt.title('He5 energies in HO for different omega values')
#ad hoc solutions to title position
#plot_title.set_y(1.03)
#plot_title.set_x(1.13)


l = range(num_energies)
for i in xrange(num_energies):
    #print omegalist, resho_mat_trans[i]
    l[i] = plt.plot(omegalist, resho_mat_trans[i])



plt.xlim([a,b])
"""for i in xrange(len(l)):
    plt.legend( (l[i]),
            ('energy level: ' + str(i)),
            'lower right')"""
plt.show() 