# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""
This script;
    Reads Probe sequence file and filter out Probes with G-Stack of exactly 4 Gs
    Generate 22 files of G-Stack probes according to the location of G-Stack in probe

"""""""""""""""""""""""""""""""""""""""
import time
from probe  import Probe
from helper import WriteToFile, findGs

def main(): 
    sequenceFile = "./../RAW_DATA/seq/seq.tab"
    outputPath   = "./../P_DATA/loc_files/from_python/"

    print("processing files ... ")    

    start_time           = time.time()
    numberOfProbes       = 0
    numberOfGstackProbes = 0

    with open(sequenceFile, encoding="utf-8") as sequenceFile:
        for line in sequenceFile:
            if numberOfProbes > 0:
                p_id, pset_id, p_x, p_y, assembly, seqname, start, stop, strand, p_seq, tar_std, cat = line.split()
                pg_loc = findGs(p_seq,'G')                
                if pg_loc > 0 and cat.find("main") != -1 :
                    numberOfGstackProbes += 1 
                    probe = Probe(pset_id, p_x, p_y, cat)
                    probe.WriteProbes(outputPath, pg_loc, True)

            numberOfProbes += 1 
    
    textToRatioFile = ""\
            + "Total No. of Probes in Seq File : \t" + str(numberOfProbes) \
            + "\nTotal No. of G-Stack Probes in Seq File : \t" + str(numberOfGstackProbes) \
            + "\nPercentage of G-Stack Probes : \t" + str(numberOfGstackProbes/numberOfProbes*100) \
            + "\nTotal no. of Probe set containing G-Stack Probes : \t" \
            + str(ProbeSetWithGstack(outputPath + "combined.txt")) \
            + "\n\nProgram took " + str(round(time.time() - start_time, 2)) + " seconds to execute."
    
    WriteToFile(outputPath + "ratio.txt", textToRatioFile)

    print("done processing ... ")




if __name__ == "__main__":
    main()
