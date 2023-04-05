import numpy as np
import confseq
from confseq.betting import *
from confseq.betting_strategies import *
from defs import *

a = np.repeat(20,n_mods)
b = np.linspace(19, 20.8,n_mods)
#mus = a/(a+b)

print("betas ", b)

dtr = np.zeros((n_ns, n_mods))
emi = np.zeros((n_ns, n_mods))
umi = np.zeros((n_ns, n_mods))
ville = np.zeros((n_ns, n_mods))

j=0
ctr = 0
for i in range(n_ns):
    for j in range(n_mods):
        for _ in range(reps):
            np.random.seed(ctr)
            x = np.random.beta(a[j], b[j], ns[i])
            
            mgale = betting_mart(x, 0.5, lambdas_fn_positive=lambda_LBOW)
            
            ville[i,j] += np.max(mgale) > 1.0/alpha
            
            mgales = []
            for l in range(B):
            	np.random.seed(ctr + i*l)
            	np.random.shuffle(x)
            	mgales.append(betting_mart(x, 0.5, lambdas_fn_positive=lambda_LBOW)[-1])
            
            csum = np.cumsum(mgales)
            
            np.random.seed(ctr)
            u = np.random.uniform(0, 1,1)[-1]
            umi[i,j] += csum[-1]/B > 1.0*u/alpha
            dtr[i,j] += csum[-1]/B > 1.0/alpha
            
            mgale_max = np.max([csum[b]/(b+1) for b in range(B)])
            emi[i,j] += mgale_max > 1.0/alpha
            
            ctr +=1

    print("dtr")
    print(dtr)
    print("umi")
    print(umi)
    print("emi")
    print(emi)
    print("ville")
    print(ville)
 
np.save("matrices/betting/power_dtr.npy", dtr)	
np.save("matrices/betting/power_umi.npy", umi)	
np.save("matrices/betting/power_emi.npy", emi)	
np.save("matrices/betting/power_ville.npy", ville)	

