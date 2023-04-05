import numpy as np
import matplotlib as matplotlib
import matplotlib.pyplot as plt
from defs import *


text_size =7.5 

matplotlib.rc('xtick', labelsize=text_size) 
matplotlib.rc('ytick', labelsize=text_size) 
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

p_dtr = np.load("matrices/e_vals/power_dtr.npy")/reps
p_umi = np.load("matrices/e_vals/power_umi.npy")/reps
p_emi = np.load("matrices/e_vals/power_emi.npy")/reps

mats = {"p_dtr": p_dtr, "p_umi": p_umi, "p_emi": p_emi}

#### Make individual plots
#
#
#for key,mat in mats.items():
#    plt.imshow(mat, cmap=cmap2)
#    plt.colorbar()
#    plt.yticks(range(M), np.round(mus,1))
#    plt.xticks(range(R), np.round(rhos,1))
#    plt.savefig("plots/e_val_" + key + ".pdf")
#    plt.clf()

### Combine above plots

from mpl_toolkits.axes_grid1 import ImageGrid


fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111,          
                 nrows_ncols=(1, 3),
                 axes_pad=0.1,      
                 direction="row",
                 #add_all=True,
                 #label_mode="1",
                 #share_all=True,
                 cbar_location="right",
                 cbar_mode="single",
                 cbar_size="10%",
                 cbar_pad=0.05,
                 )

round_mus  = np.round(mus,1)
round_rhos = np.round(rhos,1)

idm = [0,3,6,9]
idr = [0,3,6,9]

print_mus = []
for mu in round_mus[idm]:
    if mu == 0:
        print_mus.append("0")
    
    elif mu < 1:
        print_mus.append(("%.1f" % mu)[1:])
    
    elif mu == mu_max:
        print_mus.append(str(int(mu_max)))

    else:
        print_mus.append(("%.1f" % mu))

print_rhos = []
for rho in round_rhos[idr]:
    if rho == 0:
        print_rhos.append("0")
    
    elif rho == 1:
        print_rhos.append("1")

    else:
        print_rhos.append(("%.1f" % rho))

titles = ["Av+MI", "EMI", "UMI"]
i = 0
for ax, im in zip(grid, [p_dtr,p_emi,p_umi]):
    # Iterating over the grid returns the Axes.
    im = ax.imshow(im,cmap=cmap2,interpolation='none')   

    plt.sca(ax)

    plt.yticks(idm, print_mus )
    plt.xticks(idr, print_rhos)
    
    plt.title(titles[i])

    if i==0:
        plt.ylabel("$\mu$")

    plt.xlabel("$\\rho$")


    i += 1

ax.cax.colorbar(im,ticks=[0,.2,.5,.8,1])#,label=["0",".2",".5",".8","1"])
ax.cax.toggle_label(True)

plt.savefig("plots/e_val_all.pdf", bbox_inches = 'tight',pad_inches = 0)
plt.clf()

### Combine the above plots

fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111,
                 nrows_ncols=(1, 2),
                 axes_pad=0.1,
                 direction="row",
                 cbar_location="right",
                 cbar_mode="single",
                 cbar_size="10%",
                 cbar_pad=0.05,
                 )
i = 0

vmax = np.max([(p_emi-p_dtr),(p_umi-p_dtr)])

for ax, im in zip(grid, [(p_emi-p_dtr),(p_umi-p_dtr)]):
    # Iterating over the grid returns the Axes.
    im = ax.imshow(im,cmap=cmap2,interpolation='nearest',vmin=0,vmax=vmax)   

    plt.sca(ax)

    if i == 0:
        plt.title("EMI vs. Av+MI")
        plt.xlabel("$\\rho$")
        plt.ylabel("$\mu$")
    else:
        plt.title("UMI vs. Av+MI")
        plt.xlabel("$\\rho$")

    plt.yticks(idm, print_mus )
    plt.xticks(idr, print_rhos)

    i += 1

ax.cax.colorbar(im)#,ticks=[0,.2,.5,.8,1])#,label=["0",".2",".5",".8","1"])
ax.cax.toggle_label(True)

plt.savefig("plots/e_val_scaled.pdf", bbox_inches = 'tight',pad_inches = 0)
plt.clf()
