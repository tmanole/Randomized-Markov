import numpy as np
import matplotlib.pyplot as plt
from defs import *

K=100
inds = np.zeros((K,K))

def generate_e_values(mu, rho, seed):
    np.random.seed(seed)

    cov = np.zeros((K,K))
    for i in range(K):
        for j in range(K):
            cov[i,j] = rho**(np.abs(i-j))

    x = np.random.multivariate_normal(np.repeat(mu,K),cov)

    e = np.exp(x - 0.5)

    return e, x

seed = 0

p_dtr = np.empty([M, R])
p_emi = np.empty([M, R])
p_umi = np.empty([M, R])

i = 0
j = 0

for mu in mus:
    for rho in rhos:
        dtr = 0
        emi = 0 
        umi = 0

        for rep in range(reps):
            e, x = generate_e_values(mu, rho, seed)
			
            np.random.seed(seed)
            u = np.random.uniform(0, 1, 1)
			
            if np.sum(e)/K >= 1.0/alpha: 
                dtr += 1

            if np.sum(e)/K >= u/alpha:
                umi += 1

            np.random.seed(seed)
            np.random.shuffle(e)

            csum = np.cumsum(e)
            avgs = [csum[k]/(k+1) for k in range(K)]

            if np.max(avgs) >= 1.0/alpha:
                emi += 1

            seed += 1
	
        p_dtr[i,j] = dtr	
        p_umi[i,j] = umi	
        p_emi[i,j] = emi	

        print(i,j,dtr,umi,emi)

        j += 1

    j = 0 
    i += 1

np.save("matrices/Ke_vals/power_dtr.npy", p_dtr)
np.save("matrices/Ke_vals/power_umi.npy", p_umi)
np.save("matrices/Ke_vals/power_emi.npy", p_emi)
