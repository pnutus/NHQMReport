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

def calc(ordermatrix, overwrite=False):
    
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_resho_path = "data/resho"
    rel_resm_path = "data/resm"
    
    abs_resho_file_path = []
    abs_resm_file_path = []
    
    for i in xrange(len(ordermatrix)):
        abs_resho_file_path.append(os.path.join(script_dir, rel_resho_path + str(i)))
        abs_resm_file_path.append(os.path.join(script_dir, rel_resm_path + str(i)))
    
    
    try:
        for file in abs_resho_file_path + abs_resm_file_path:
            open(file)
            if overwrite:
                raise IOError 
            
            resho_mat = []
            resm_mat = []
            
            for i in xrange(len(abs_resm_file_path)):
                resho_mat.append( sp.load(abs_resho_file_path[i]))
                resm_mat.append( sp.load(abs_resm_file_path[i]))
            
            return resho_mat, resm_mat
            
    except IOError:
        print "calculating"
    
        mom.integration_order = 20
        mom.integration_range = 10
        osc.integration_order = 60
        
        resho_mat =[]
        resm_mat=[]

        problem = H_atom
        omega =1
        problem.HO_omega = omega


        for i, orderlist in enumerate(ordermatrix):
            #print orderlist
            resho = []
            resm = []
            for order in orderlist:

                Q = osc.QNums(l=0, j=.5, n=range(order))
                H = osc.hamiltonian(order, problem, Q)
                eigvals, eigvecs = energies(H)
                #print osc.name, eigvals[0], problem.units
                resho.append(eigvals[0])
    
                contour = gauss_contour([0, 5], order)
                H = mom.hamiltonian(contour, problem, Q)
                eigvals, eigvecs = energies(H)
                #print mom.name, eigvals[0], problem.units
                resm.append(eigvals[0])
                
            sp.save(abs_resho_file_path[i], resho)
            sp.save(abs_resm_file_path[i], resm)   
                 
            resho_mat.append(resho)
            resm_mat.append(resm)
     
        return resho_mat, resm_mat        

