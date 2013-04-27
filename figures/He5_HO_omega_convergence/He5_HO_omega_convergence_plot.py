from __future__ import division
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
import He5_HO_omega_convergence_data as data

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

osc.integration_order = 60
He5.V0 = -52

#omegalist =[1,2,3,4,5,6,7,8,9,10]
omegalist= [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]

num_energies=5
resho_mat = data.calc(omegalist, num_energies, order=20, overwrite=False)
resho_mat_trans = zip(*resho_mat)


plts.plot_init(font_size=14,tick_size=11) #set font sizes.
fig = plt.figure()


plt.ylabel('energy [MeV]')
plt.xlabel('omega')
plot_title=plt.title('He5 energies in HO for different omega values')
#ad hoc solutions to title position
plot_title.set_y(1.03)
#plot_title.set_x(1.13)


l = range(num_energies)
for i in xrange(num_energies):
    #print omegalist, resho_mat_trans[i]
    l[i] = plt.plot(omegalist, resho_mat_trans[i])



plt.xlim([lmin(omegalist), lmax(omegalist)])
"""for i in xrange(len(l)):
    plt.legend( (l[i]),
            ('energy level: ' + str(i)),
            'lower right')"""
    
plt.show() 