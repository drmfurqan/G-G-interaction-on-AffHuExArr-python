#coding: utf-8

import numpy as np
import os

# reading probe set id of all G-stack Probes 
g_ps = np.genfromtxt("d:/PYPELINE/HuEx/P_DATA/loc_files/all_G_Probes.txt", usecols = (2))

# Reading All probes from Probe Sequence File (Columns to read 1: Probe set ID, 2: Probe x, 3: Probe y)
all_probes = np.genfromtxt("d:/PYPELINE/HuEx/RAW_DATA/seq/seq.tab", skip_header = 1, usecols = (1,2,3)).astype(int)

# Filtering all Probes which have no G-stack probe
not_G_probes = all_probes[np.setdiff1d(all_probes[:,0], g_ps), :]

#Saving probes sequence data of all non G Probe sets
np.savetxt("d:/PYPELINE/HuEx/P_DATA/alt_p_data/not_G_Probeset.csv", not_G_probes, fmt='%d', delimiter=',', header="Probeset_id, x, y")


#Selecting Probe Sets having only 1 G-stack Probe and 3 non G-stack probes
temp = not_G_probes[:,0]
u, ind, count = np.unique(temp, return_index=True, return_counts=True)
x = [ind[i] for i in range(len(count)) if count[i] == 4]
ups4 = temp[x]
i = np.in1d(all_probes[:,0], ups4)
not_G_4probes = all_probes[i, :]

#Saving all probes sequence data of  Probe sets of exactly 4 probes
np.savetxt("d:/PYPELINE/HuEx/P_DATA/alt_p_data/Not_G_probeset_all_Probes.csv", not_G_4probes, fmt='%d', delimiter=',', header="Probeset_id, x, y")

