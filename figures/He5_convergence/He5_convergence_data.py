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

def calc(orderlist, overwrite=False):
    
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_resho_path = "data/resho"
    rel_resm_path = "data/resm"
    
    abs_resho_file_path = []
    abs_resm_file_path = []
    

    
    mom.integration_order = 20
    mom.integration_range = 10
    osc.integration_order = 60
    
    resho_mat =[]
    resm_mat=[]

    problem = He5



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
 
         
    return resho, resm        

