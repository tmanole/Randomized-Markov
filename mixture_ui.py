import numpy as np
from fmix import *
from scipy.stats import chi2
from defs import *

n = 500
n2 = int(n/2)

p_lrt        = np.zeros((n_mods,reps))
p_ui         = np.zeros((n_mods,reps))
p_umi_ui     = np.zeros((n_mods,reps))
p_sub_ui     = np.zeros((n_mods,reps))
p_umi_sub_ui = np.zeros((n_mods,reps))
p_emi_sub_ui = np.zeros((n_mods,reps))
p_rmi_sub_ui = np.zeros((n_mods,reps))

# 1-alpha quantile of (1/2) \chi_0^2 + (1/2) \chi_1^2
qchi = chi2.ppf(1-2.0*alpha,1)  

j=0
ctr = 0
for rep in range(reps):
    for j in range(n_mods):
        e = eps[j]

        np.random.seed(ctr)
        x = sample_mixture(-e,e,v0,pi0,n)

        np.random.seed(ctr)
        u = np.random.uniform(0,1,1)

        ## LRT
        (_,_,full_lik,_) = fit_mixture(x,-e, e,pi0,v0,n_starts=15)    
        null_lik = null_likelihood(x,np.sum(x)/n,v0)
        lrt = np.max([0,-2 * (null_lik - full_lik) ])

        p_lrt[j,rep] = lrt > qchi
        
        ## UI
        slrt = split_lrt(x,-e,e, pi0=pi0, v0=v0, n_starts=n_starts)
        p_ui[j,rep] = slrt > 1.0/alpha 

        ## UMI UI
        p_umi_ui[j,rep] = slrt > u/alpha

        ## Subsampling UI
        sub_slrt = sub_ui(x,-e,e, pi0=pi0, v0=v0, n_starts=n_starts)
        p_sub_ui[j,rep] = sub_slrt[-1] > 1.0/alpha     

        ## UMI Subsampling UI
        p_umi_sub_ui[j,rep] = sub_slrt[-1] > u/alpha     

        ## EMI Subsampling UI
        p_emi_sub_ui[j,rep] = np.max(sub_slrt) > 1.0/alpha     

        ## EMI+UMI Subsampling UI
        p_rmi_sub_ui[j,rep] = (sub_slrt[0] > u/alpha) or (np.max(sub_slrt) > 1.0/alpha)
        
        ctr +=1

    if rep % 10 == 0:
        print("lrt  ", np.sum(p_lrt,axis=1))
        print("UI   ", np.sum(p_ui,axis=1))
        print("UUI  ", np.sum(p_umi_ui,axis=1))
        print("SUI  ", np.sum(p_sub_ui,axis=1))
        print("SUMI ", np.sum(p_umi_sub_ui,axis=1))
        print("SEMI ", np.sum(p_emi_sub_ui,axis=1))
        print("SEUMI", np.sum(p_rmi_sub_ui,axis=1))

np.save("matrices/ui/power_lrt.npy", p_lrt)	
np.save("matrices/ui/power_ui.npy", p_ui)	
np.save("matrices/ui/power_umi_ui.npy", p_umi_ui)	
np.save("matrices/ui/power_sub_ui.npy", p_sub_ui)	
np.save("matrices/ui/power_umi_sub_ui.npy", p_umi_sub_ui)	
np.save("matrices/ui/power_emi_sub_ui.npy", p_emi_sub_ui)	
np.save("matrices/ui/power_rmi_sub_ui.npy", p_rmi_sub_ui)	
