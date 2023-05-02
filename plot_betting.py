import numpy as np
import matplotlib as matplotlib
import matplotlib.pyplot as plt
#import matplotlib.colors as colors
#from matplotlib.colors import LinearSegmentedColormap
from defs import *


text_size =7.5 

matplotlib.rc('xtick', labelsize=text_size) 
matplotlib.rc('ytick', labelsize=text_size) 
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

p_ville = np.load("matrices/betting/power_ville.npy")/reps
p_dtr = np.load("matrices/betting/power_dtr.npy")/reps
p_umi = np.load("matrices/betting/power_umi.npy")/reps
p_emi = np.load("matrices/betting/power_emi.npy")/reps
p_rmi = np.load("matrices/betting/power_emi.npy")/reps

mats = {"p_ville": p_ville, "p_dtr": p_dtr, "p_umi": p_umi, "p_emi": p_emi, "p_rmi": p_rmi}

### Make individual plots


#for key,mat in mats.items():
#    plt.imshow(mat, cmap="Greys")
#    plt.colorbar()
#    plt.yticks(range(n_ns), ns)
#    plt.xticks(range(n_mods), np.round(b,1))
#    plt.savefig("plots/betting_" + key + ".pdf")
#    plt.clf()

### Combine above plots

from mpl_toolkits.axes_grid1 import ImageGrid


fig = plt.figure(1,figsize=(4.,4.))
grid = ImageGrid(fig, 111,          
                 nrows_ncols=(1,3),
                 axes_pad=0.1,      
                 direction="row",
                 cbar_location="right",
                 cbar_mode="single",
                 cbar_size="10%",
                 cbar_pad=0.05
                 )

round_ns = ns
#round_ns  = np.round(ns,1)
round_bs = np.round(b,1)

idm = [0,3,6,9]
idr = [1,5,8]

print_ns = round_ns[idm]
print_bs = round_bs[idr]

i = 0
titles= ["Av+MI","Ville","EMI"]
the_ps = [p_dtr,p_ville,p_emi,p_umi,p_rmi]
for ax, im in zip(grid, the_ps):
    im = ax.imshow(im,cmap=cmap2,interpolation='nearest',vmin=0,vmax=np.max(the_ps))   

    plt.sca(ax)

    plt.yticks(idm, print_ns, fontsize=5)
    plt.xticks(idr, print_bs, fontsize=5)

    if i == 0:
        plt.ylabel("$n$")

    plt.xlabel("$b$")
    plt.title(titles[i])
    i += 1

ax.cax.colorbar(im)#,ticks=[0,.2,.5,.8,1])#,label=["0",".2",".5",".8","1"])
ax.cax.toggle_label(True)

plt.savefig("plots/betting_all1.pdf", bbox_inches = 'tight',pad_inches = 0)
plt.clf()

fig = plt.figure(1,figsize=(4.,4.))
grid = ImageGrid(fig, 111,          
                 nrows_ncols=(1,3),
                 axes_pad=0.1,      
                 direction="row",
                 )

i = 0
titles= ["UMI","EUMI",""]
the_ps = [p_umi,p_rmi,p_rmi]
for ax, im in zip(grid, the_ps):
    im = ax.imshow(im,cmap=cmap2,interpolation='nearest',vmin=0,vmax=np.max(the_ps))   

    plt.sca(ax)

    plt.yticks(idm, print_ns, fontsize=5)
    plt.xticks(idr, print_bs, fontsize=5)

    if i == 0:
        plt.ylabel("$n$")

    plt.xlabel("$b$")
    plt.title(titles[i])
    i += 1

ax.set_visible(False)

#ax.cax.colorbar(im)#,ticks=[0,.2,.5,.8,1])#,label=["0",".2",".5",".8","1"])
ax.cax.toggle_label(True)

plt.savefig("plots/betting_all2.pdf", bbox_inches = 'tight',pad_inches = 0)
plt.clf()

### Plot differences in power between EMI & MI or Ville 

idm = [0,3,6,9]
idr = [0,5,9]

print_ns = round_ns[idm]
print_bs = round_bs[idr]

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
    
vmax=np.max([p_umi-p_dtr,p_umi-p_ville]) #0.082#np.max([p_emi-p_ville,p_emi-p_dtr])
vmin=-vmax

for ax, im in zip(grid, [(p_emi-p_dtr),(p_emi-p_ville)]):
    im = ax.imshow(im, interpolation="nearest",cmap="bwr",vmin=vmin,vmax=vmax)

    plt.sca(ax)

    plt.yticks(idm, print_ns)
    plt.xticks(idr, print_bs)

    if i == 1:
        plt.title("EMI vs. Ville")
        plt.xlabel("$b$")

    else:
        plt.title("EMI vs. Av+MI")
        plt.xlabel("$b$")
        plt.ylabel("$n$")

    i += 1

ax.cax.colorbar(im)#,ticks=np.round(np.linspace(vmin,vmax,4),2))#,label=["0",".2",".5",".8","1"])
ax.cax.toggle_label(True)
plt.savefig("plots/betting_diffs_EMI.pdf", bbox_inches = 'tight',pad_inches = 0)
plt.clf()

### Plot differences in power between UMI & MI or Ville 

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
    
for ax, im in zip(grid, [(p_umi-p_dtr),(p_umi-p_ville)]):
    im = ax.imshow(im, interpolation="nearest",vmin=0,vmax=vmax,cmap=cmap2)

    plt.sca(ax)

    plt.yticks(idm, print_ns)
    plt.xticks(idr, print_bs)

    if i == 1:
        plt.title("UMI vs. Ville")
        plt.xlabel("$b$")

    else:
        plt.title("UMI vs. Av+MI")
        plt.xlabel("$b$")
        plt.ylabel("$n$")

    i += 1

ax.cax.colorbar(im)#ticks)#=[vmin,0,.2,.5,.8,vmax])#,label=["0",".2",".5",".8","1"])
ax.cax.toggle_label(True)

plt.savefig("plots/betting_diffs_UMI.pdf", bbox_inches = 'tight',pad_inches = 0)
plt.clf()

### Plot differences in power between UMI & MI or Ville 

fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111,
                 nrows_ncols=(1, 1),
                 axes_pad=0.1,
                 direction="row",
                 cbar_location="right",
                 cbar_mode="single",
                 cbar_size="10%",
                 cbar_pad=0.05,
                 )

ax = grid[0]

im = p_ville - p_dtr    
im = ax.imshow(im, interpolation="nearest",vmin=0,vmax=np.max(im),cmap=cmap2)

plt.sca(ax)

plt.yticks(idm, print_ns)
plt.xticks(idr, print_bs)
plt.title("Ville vs. Av+MI")
plt.xlabel("$b$")
plt.ylabel("$n$")


ax.cax.colorbar(im)#ticks)#=[vmin,0,.2,.5,.8,vmax])#,label=["0",".2",".5",".8","1"])
ax.cax.toggle_label(True)

plt.savefig("plots/betting_diffs_Ville_MI.pdf", bbox_inches = 'tight',pad_inches = 0)
plt.clf()


### Plot differences in power between EUMI & MI or Ville 

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
   
print(p_emi-p_rmi)
for ax, im in zip(grid, [(p_rmi-p_dtr),(p_rmi-p_ville)]):
    im = ax.imshow(im, interpolation="nearest",vmin=-vmax,vmax=vmax,cmap="bwr")

    plt.sca(ax)

    plt.yticks(idm, print_ns)
    plt.xticks(idr, print_bs)

    if i == 1:
        plt.title("EUMI vs. Ville")
        plt.xlabel("$b$")

    else:
        plt.title("EUMI vs. Av+MI")
        plt.xlabel("$b$")
        plt.ylabel("$n$")

    i += 1

ax.cax.colorbar(im)#ticks)#=[vmin,0,.2,.5,.8,vmax])#,label=["0",".2",".5",".8","1"])
ax.cax.toggle_label(True)

plt.savefig("plots/betting_diffs_EUMI.pdf", bbox_inches = 'tight',pad_inches = 0)
plt.clf()

