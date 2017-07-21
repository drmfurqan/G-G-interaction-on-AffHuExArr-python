# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""
This script;
    Reads location wise intensity matrices to ;
        to calculate average correlation between 22 group of matrices
    Store average correlation coefficient in a 22 x 22 matrix        
"""""""""""""""""""""""""""""""""""""""
import numpy as np
import time


# ------------ main starts --------------------- #
def main():
    start_time = time.time()
    
    cor_m = np.zeros((22,22))

    mlist = list(range(22))
    
    path = "./../P_DATA/matrices/" 
    f_pre = "m"
    ext = ".csv"

    for i in mlist : 
        print("Reading location no." + str( i+1 ) + " matrix.")
        file = path + f_pre + str(i+1) + ext
        mlist[i] = list(np.genfromtxt(file, delimiter=','))       
    
    for i in range(22) : 
        g1 = mlist[i]
        for j in range(i, 22) :
            print("processing now i : "+str(i+1)+ " and j : "+str(j+1))
            if i == j : 
                cor_m[j,i] = cor_m[i,j] = avgcor(np.corrcoef(g1))
            else : 
                g2 = mlist[j]
                cor_m[j,i] = cor_m[i,j] = avgcor2(g1,g2)
    
    np.savetxt("./../RESULTS/Corr_Matrix.csv", cor_m, delimiter = ',')
    print("--- %s seconds ---" % round(time.time() - start_time, 2))

# ------------------ main ends here ------------------------- #




# ------------------ functions definitions ------------------ #

avgcor = lambda x : np.mean(x[np.tril_indices_from(x, -1)]) # avg correlation for same group


# avgcor2 function calculates avg correlation between different group
def avgcor2 (x, y) :
    ksum = 0
    n = np.asmatrix(x)[:, 0].size
    
    for k in range(0, n) :
        c =  np.corrcoef(np.asmatrix(list([x[k]] + y)))
        ksum += np.mean(c[0, 1: ])

    a = ksum / n
    return (a)

# ---------------- functions definitions end here --------------- #


# ----------------- executing main -------------------- #
if __name__ == "__main__":
    main()