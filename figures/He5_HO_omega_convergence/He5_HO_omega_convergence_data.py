from __future__ import division
#from imports import *
from nhqm.bases import harm_osc as osc, mom_space as mom
from nhqm.problems import H_atom, He5
from nhqm.QM_helpers import energies
from nhqm.bases.gen_contour import gauss_contour
import plot_setup as plts
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import os
import scipy as sp

def calc(omegalist, num_energies, order, overwrite=False):
    
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_resho_path = "data/resho_omega"
    
    abs_resho_file_path = []
    
    for i in xrange(len(omegalist)):
        abs_resho_file_path.append(os.path.join(script_dir, rel_resho_path + str(i)+'.npy'))
        
    
    
    try:
        for file in abs_resho_file_path:
            open(file)
            if overwrite:
                raise IOError 
            
            resho_mat = []
            
            for i in xrange(len(abs_resho_file_path)):
                resho_mat.append( sp.load(abs_resho_file_path[i]))
                
            return resho_mat
            
    except IOError:
        print "calculating"
        osc.integration_order = 60
        
        resho_mat =[]

        problem = He5


        for i, omega in enumerate(omegalist):
            He5.HO_omega = omega
            energies_for_omega = []

            Q = osc.QNums(l=1, j=1.5, n=range(order))
            H = osc.hamiltonian(order, problem, Q)
            eigvals, eigvecs = energies(H)
            
            for j in xrange(num_energies):
                energies_for_omega.append(eigvals[j])
                
            sp.save(abs_resho_file_path[i], energies_for_omega)
            resho_mat.append(energies_for_omega)
        return resho_mat  

