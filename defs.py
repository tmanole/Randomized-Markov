import numpy as np

### Global defs
alpha = 0.05
reps = 500
n_ns = 10
n_mods = 10
ns = np.linspace(100, 2000, n_ns, dtype=int)
B = 100

### E-value defs
M = 10
R = 10
mu_max = 4
rho_max = 1
mus = np.linspace(0, mu_max, M)
rhos = np.linspace(0, rho_max, R)

### Betting defs
a = np.repeat(20,n_mods)
b = np.linspace(19, 20.8,n_mods)

### Interval defs
interval_reps = 20000

### Universal Inference defs
e_max = 1  # e = \mu in the notation of the paper
eps = np.linspace(0,e_max,n_mods)
pi0 = 0.25
v0 = 1
n_starts = 5

### Plotting
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
cmap = plt.get_cmap('bwr')
colors = cmap(np.linspace(0.5, 1, cmap.N // 2))
cmap2 = LinearSegmentedColormap.from_list('Upper Half', colors)


