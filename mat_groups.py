# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""
This script;
    Reads loc files to ;
        calculate composite value
        store cv of every loc file in loc_list (list object)
    Reads Cel files to;
        to filter mean intensitie values of probes in loc_list
        to store location wise intensity matrices
"""""""""""""""""""""""""""""""""""""""

import os
import numpy as np
import time


def main():
    start_time = time.time()            
    loc_list = list(range(22))    
    for i in range(22):
        filename = "./../P_DATA/loc_files/loc" + str(i+1) + ".txt"
        print("processing loc", i+1)

        loc = np.genfromtxt(filename)
        loc_c = (loc[:,0] + (2560 * loc[:,1]))
        loc_c = list(map(int, loc_c))

        loc_list[i] = loc_c

    cel_path = "./../RAW_DATA/cel_files/"
    cel_files = [f for f in os.listdir(cel_path) if f.find("GSM") >= 0]

    mlist = list(range(22))
    for i in range(22):
      mat = np.zeros((len(loc_list[i]), len(cel_files)))
      mlist[i] = mat

    n = 0
    for file in cel_files:
        print (file)
        data_cel = np.genfromtxt(cel_path + file, skip_header = 24, max_rows = 6553600, usecols = (2))
        m = np.log(data_cel) - np.mean(np.log(data_cel))
        for i in range(22):
            print("processing now location: " + str(i+1))
            mlist[i][:,n] = m[loc_list[i]]
        
        n += 1


    for i in range(22):
        filename = "./../P_DATA/matrices/m" + str(i+1) + ".csv"
        np.savetxt(filename, mlist[i], delimiter = ',')

    print("--- %s seconds ---" % round(time.time() - start_time, 2))

if __name__ == "__main__":
    main()
