import numpy as np
from scipy.stats import norm 
from defs import *

reps = interval_reps

c_chb = np.zeros((n_ns,reps))
c_hof = np.zeros((n_ns,reps))
c_umi = np.zeros((n_ns,reps))
c_opt = np.zeros((n_ns,reps))

l_chb = np.zeros((n_ns,reps))
l_hof = np.zeros((n_ns,reps))
l_umi = np.zeros((n_ns,reps))
l_opt = np.zeros((n_ns,reps))


zalpha = norm.ppf(1-alpha/2.0)

j=0
ctr = 0
for i in range(n_ns):
    print(i)
    for rep in range(reps):
        n = ns[i]

        np.random.seed(ctr)
        x = np.random.normal(0,1,n)
        xbar = np.sum(x)/n
        np.random.seed(ctr)
        u = np.random.uniform(0,1,1)

        bdry_opt = zalpha/np.sqrt(n)
        bdry_chb = 1/np.sqrt(alpha * n)
        bdry_hof = np.sqrt(2 * np.log(2.0/alpha) / n)
        bdry_umi = np.sqrt(np.log(2.0/alpha)/(2.0*n)) + np.log(2.0*u/alpha) / np.sqrt(2.0 * n * np.log(2.0/alpha)) 

        l_opt[i,rep] += 2 * bdry_opt
        l_chb[i,rep] += 2 * bdry_chb
        l_hof[i,rep] += 2 * bdry_hof
        l_umi[i,rep] += 2 * bdry_umi

        c_opt[i,rep] += np.abs(xbar) <= bdry_opt
        c_chb[i,rep] += np.abs(xbar) <= bdry_chb
        c_hof[i,rep] += np.abs(xbar) <= bdry_hof
        c_umi[i,rep] += np.abs(xbar) <= bdry_umi

        ctr +=1

    i+=1


#print("l_opt: ", l_opt)
#print("chb  :", l_chb)
#print("hof", l_hof)
#print("umi", l_umi)
#
#print(np.vstack([l_opt, l_umi, l_hof]))
#print("----")
#print(l_opt/l_umi)
#print("====")
#print(l_umi/l_hof)
#
#
#print(c_opt)

np.save("matrices/intervals/l_chb.npy", l_chb)	
np.save("matrices/intervals/l_umi.npy", l_umi)	
np.save("matrices/intervals/l_hof.npy", l_hof)	
np.save("matrices/intervals/l_opt.npy", l_opt)	

np.save("matrices/intervals/c_chb.npy", c_chb)	
np.save("matrices/intervals/c_umi.npy", c_umi)	
np.save("matrices/intervals/c_hof.npy", c_hof)	
np.save("matrices/intervals/c_opt.npy", c_opt)	

