import numpy as np
import matplotlib.pyplot as plt
from defs import *
import pathlib

pathlib.Path("matrices/e_vals").mkdir(parents=True, exist_ok=True) 

def generate_e_values(mu, rho, seed):
	cov = np.array([[1,rho],[rho,1]])
	np.random.seed(seed)
	x1,x2 = np.random.multivariate_normal([mu,mu],cov)

	e1 = np.exp(x1-0.5)
	e2 = np.exp(x2-0.5)

	return e1, e2, x1, x2

seed = 0

p_dtr = np.empty([M, R])
p_emi = np.empty([M, R])
p_umi = np.empty([M, R])
p_rmi = np.empty([M, R]) # EMI + UMI

i = 0
j = 0

for mu in mus:
	for rho in rhos:
		dtr = 0
		emi = 0
		umi = 0
		rmi = 0

		for rep in range(reps):
			e1,e2, x1,x2 = generate_e_values(mu, rho, seed)
			
			np.random.seed(seed)
			u = np.random.uniform(0, 1, 1)
			
			np.random.seed(seed)
			k = np.random.binomial(1, 0.5, 1)

			pe1 = e1
			pe2 = e2

			if k==1:
				pe1 = e2
				pe2 = e1

			seed += 1

			if (e1+e2)/2 >= 1.0/alpha:
				dtr += 1

			if (e1+e2)/2 >= u/alpha:
				umi += 1

			if pe1 >= 1.0/alpha or (pe1+pe2)/2 >= 1.0/alpha:
				emi += 1

			if pe1 >= u/alpha or (pe1+pe2)/2 >= 1.0/alpha:
				rmi += 1

		
		p_dtr[i,j] = dtr	
		p_umi[i,j] = umi	
		p_emi[i,j] = emi	
		p_rmi[i,j] = rmi	

		j += 1
	j = 0
	i += 1



print(p_dtr/reps)
print(p_emi/reps)
print(p_umi/reps)
print(p_rmi/reps)

np.save("matrices/e_vals/power_dtr.npy", p_dtr)
np.save("matrices/e_vals/power_umi.npy", p_umi)
np.save("matrices/e_vals/power_emi.npy", p_emi)
np.save("matrices/e_vals/power_rmi.npy", p_rmi)
