import numpy as np
import matplotlib as matplotlib
import matplotlib.pyplot as plt
#import matplotlib.colors as colors
from matplotlib.colors import LinearSegmentedColormap
from defs import *

reps=interval_reps 
text_size = 17

matplotlib.rc('xtick', labelsize=text_size) 
matplotlib.rc('ytick', labelsize=text_size) 
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

#matplotlib.rcParams['figure.figsize'] = (6,6)

lw = 3
elw=0.8


### Plot length

fig = plt.figure()


l_hof = np.load("matrices/intervals/l_hof.npy")
l_umi = np.load("matrices/intervals/l_umi.npy")
l_opt = np.load("matrices/intervals/l_opt.npy")

l_umi[l_umi <0] = 0 

lll = l_umi[-1,:]
print(np.max(lll))
print(np.min(lll))
print(np.quantile(lll,0.25))

#yerr = 2 * np.std(l_umi, axis=1)

y_umi = np.sum(l_umi, axis=1)/reps
y_hof = np.sum(l_hof, axis=1)/reps
y_opt = np.sum(l_opt, axis=1)/reps

plt.plot(ns, y_umi, lw=lw, label="Randomized Hoeffding")
plt.plot(ns, y_hof, lw=lw, label="Hoeffding")
plt.plot(ns, y_opt, lw=lw, label="Exact (Central Limit Theorem)")

plt.xlabel("$n$",fontsize=text_size)
plt.ylabel("Interval width",fontsize=text_size)

handles, labels = plt.gca().get_legend_handles_labels()
order = [1,0,2]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc="upper right", prop={'size':text_size})

#plt.legend(loc="upper right", title="", prop={'size':text_size})

plt.grid(True,alpha=.5)

plt.savefig("plots/interval_length.pdf", bbox_inches = 'tight',pad_inches = 0)
plt.clf()


### Plot coverage

fig = plt.figure()


c_hof = np.load("matrices/intervals/c_hof.npy")
c_umi = np.load("matrices/intervals/c_umi.npy")
c_opt = np.load("matrices/intervals/c_opt.npy")

yerr = 2 * np.std(l_umi, axis=1)

y_umi = np.sum(c_umi, axis=1)/reps
y_hof = np.sum(c_hof, axis=1)/reps
y_opt = np.sum(c_opt, axis=1)/reps

plt.plot(ns, y_umi, lw=lw, label="Randomized Hoeffding")
plt.plot(ns, y_hof, lw=lw, label="Hoeffding")
plt.plot(ns, y_opt, lw=lw, label="Exact (Central Limit Theorem)")

plt.xlabel("$n$",fontsize=text_size)
plt.ylabel("Coverage (\%)",fontsize=text_size)

#handles, labels = plt.gca().get_legend_handles_labels()
#order = [1,0,2]
#plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc="upper right", prop={'size':text_size})
#
##plt.legend(loc="upper right", title="", prop={'size':text_size})

plt.grid(True,alpha=.5)

plt.savefig("plots/interval_coverage.pdf", bbox_inches = 'tight',pad_inches = 0)
plt.clf()



