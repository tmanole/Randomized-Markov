# This file is adapted from https://github.com/tmanole/Gaussian-mixture-twocomp/blob/master/python/functions.py

import numpy as np

def sample_mixture(mu1, mu2, v, pi, n):
    """ Sample from the mixture. """
    x = np.empty(n)

    for i in range(n):
        u = np.random.uniform(size=1)

        if u < pi:
            x[i] = np.random.normal(loc=mu1, scale=np.sqrt(v), size=1)

        else:
            x[i] = np.random.normal(loc=mu2, scale=np.sqrt(v), size=1)

    return x


def density(y, mu, v):
    """ Gaussian density, without normalizing constant. """
    return np.exp(-(y-mu)**2/(2*v))/np.sqrt(2*np.pi*v)

def likelihood(Y, mu1, mu2, v, pi):
    """ Likelihood function, up to normalization. """
    return np.sum(np.log(pi * density(Y, mu1, v) + (1-pi) * density(Y, mu2, v)))

def null_likelihood(Y, mu, v):
    """ Likelihood function, up to normalization. """
    return np.sum(np.log(density(Y, mu, v)))


def em(Y, pi, mu1_start, mu2_start, v, max_iter=2000, eps=1e-8):
    """ EM Algorithm. """
    n = Y.size

    mu1_new = mu1_start
    mu2_new = mu2_start

    for j in range(max_iter):

        denom = pi * density(Y, mu1_new, v) + (1-pi) * density(Y, mu2_new, v)
        weights1 = pi * density(Y, mu1_new, v) / denom
        weights2 = 1-weights1

        w_sum = np.sum(weights1)

        mu1_old = mu1_new
        mu2_old = mu2_new
        mu1_new = np.sum(weights1 * Y)/(w_sum)
        mu2_new = np.sum(weights2 * Y)/(n-w_sum)

        lik = likelihood(Y, mu1_new, mu2_new, v, pi)
        stopping_criterion = np.abs(likelihood(Y, mu1_old, mu2_old, v, pi) - lik)

        if stopping_criterion < eps:
            break

    return (mu1_new, mu2_new, lik, j)



def fit_mixture(x, mu1,mu2,pi0, v0, n_starts=10):
    full_lik = np.NINF
    ctr = 0
    n = x.size

    for s in range(n_starts):
        np.random.seed(2*ctr)
        noise_mu1 = np.random.normal(0,n**(-1.0/8),1)

        np.random.seed(2*ctr + 1)
        noise_mu2 = np.random.normal(0,n**(-1.0/8),1)

        (mu1_hat_t,mu2_hat_t,full_lik_t,iters_t) = em(x,pi0,mu1+noise_mu1,mu2+noise_mu2,v0)
        if full_lik_t > full_lik:
            full_lik = full_lik_t
            mu1_hat = mu1_hat_t
            mu2_hat = mu2_hat_t
            iters = iters_t

        ctr += 1

    return (mu1_hat, mu2_hat, full_lik, iters)

def split_lrt(x,mu1,mu2,pi0,v0,n_starts=10):
    n = x.size
    n2 = int(n/2)

    (hmu1,hmu2,_,_) = fit_mixture(x[n2:],mu1, mu2,pi0,v0,n_starts)

    numer = np.exp(likelihood(x[:n2],hmu1,hmu2,v0,pi0))
    denom = np.exp(null_likelihood(x[:n2], np.sum(x[:n2])/n2, v0))
 
    return numer/denom
    
def sub_ui(x, mu1, mu2, pi0, v0, n_starts=10, B=100):
    uis = []
    ctr = 99999

    for b in range(B):
        np.random.seed(ctr)
        np.random.shuffle(x)
        uis.append(split_lrt(x,mu1,mu2,pi0,v0,n_starts))

    csum = np.cumsum(uis)

    return [csum[k]/(k+1) for k in range(B)]

   

