import numpy as np
import matplotlib as matplotlib
import matplotlib.pyplot as plt
#import matplotlib.colors as colors
from matplotlib.colors import LinearSegmentedColormap
from defs import *

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


fig = plt.figure()

p_lrt        = np.load("matrices/ui/power_lrt.npy")
p_ui         = np.load("matrices/ui/power_ui.npy")       
p_umi_ui     = np.load("matrices/ui/power_umi_ui.npy")       
p_sub_ui     = np.load("matrices/ui/power_sub_ui.npy")       
p_umi_sub_ui = np.load("matrices/ui/power_umi_sub_ui.npy")       
p_emi_sub_ui = np.load("matrices/ui/power_emi_sub_ui.npy")   

y_lrt        = np.sum(p_lrt       , axis=1)/reps       
y_ui         = np.sum(p_ui        , axis=1)/reps       
y_umi_ui     = np.sum(p_umi_ui    , axis=1)/reps
y_sub_ui     = np.sum(p_sub_ui    , axis=1)/reps
y_umi_sub_ui = np.sum(p_umi_sub_ui, axis=1)/reps
y_emi_sub_ui = np.sum(p_emi_sub_ui, axis=1)/reps

print(y_lrt)

#yerr = 2 * np.std(l_umi, axis=1)

plt.plot(eps, y_lrt, lw=lw, label="LRT")
plt.plot(eps, y_ui, lw=lw, label="UI")
plt.plot(eps, y_umi_ui, lw=lw, label="UMI-UI")
plt.plot(eps, y_sub_ui, lw=lw, label="SUI")
plt.plot(eps, y_umi_sub_ui, lw=lw, label="UMI-SUI")
plt.plot(eps, y_emi_sub_ui, lw=lw, label="EMI-SUI")

plt.xlabel("$\mu$",fontsize=text_size)
plt.ylabel("Proportion of Rejections",fontsize=text_size)

#handles, labels = plt.gca().get_legend_handles_labels()
#order = [1,0,2]
#plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc="upper right", prop={'size':text_size})

plt.legend(loc="lower right", title="", prop={'size':text_size})

plt.grid(True,alpha=.5)

plt.savefig("plots/ui_power.pdf", bbox_inches = 'tight',pad_inches = 0)
plt.clf()

