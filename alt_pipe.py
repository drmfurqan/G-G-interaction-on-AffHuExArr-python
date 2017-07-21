
# coding: utf-8

import numpy as np


# reading probe set id of all G-stack Probes 
#aps = all probe set

aps = np.genfromtxt("e:/PYPELINE/HuEx/P_DATA/loc_files/all_G_Probes.txt", usecols = (2))


#Selecting Unique Probe Sets having only 1 G-stack Probe
#ups = unique probe set


u, ind, count = np.unique(aps, return_index=True, return_counts=True)

x = [ind[i] for i in range(len(count)) if count[i] == 1]

ups = aps[x]


# Saving file to disk

np.savetxt("e:/PYPELINE/HuEx/P_DATA/loc_files/UNI.txt", ups, fmt='%d')


# Reading All probes from Probe Sequence File (Columns to read 1: Probe set ID, 2: Probe x, 3: Probe y)

all_probes = np.genfromtxt("e:/PYPELINE/HuEx/RAW_DATA/seq/seq.tab", skip_header = 1, usecols = (1,2,3))


# Getting index of Unique Probe set in all_probes

i = np.in1d(all_probes[:,0], ups)


# Selecting all probes of Unique Probe sets
ups_probes = all_probes[i, :]


#Saving all probes data of Unique Probe sets

np.savetxt("e:/PYPELINE/HuEx/P_DATA/loc_files/UPS_PROBE.csv", ups_probes, fmt='%d', delimiter=',')



#Selecting Unique Probe Sets having only 1 G-stack Probe and 3 non G-stack probes

temp = ups_probes[:,0]

u, ind, count = np.unique(temp, return_index=True, return_counts=True)

x = [ind[i] for i in range(len(count)) if count[i] == 4]

ups4 = temp[x]

i = np.in1d(all_probes[:,0], ups4)
ups_4probes = all_probes[i, :]


#Saving all probes data of Unique Probe sets of exactly 4 probes

np.savetxt("e:/PYPELINE/HuEx/P_DATA/loc_files/UPS_4PROBE.csv", ups_4probes, fmt='%d', delimiter=',')

