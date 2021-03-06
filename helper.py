def WriteToFile(filename, lineToWrite):
        """
        helper function
        Takes two aurgements 
        \n1. filename (string with valid filepath)
        \n2. lineToWrite (stirng to write on file)
        Files are opened in append mode to avoid overwirte. 
        """
        with open(filename, mode="a", encoding="utf-8") as f:
            f.write(lineToWrite)



def FindNTstack(sequence, nt):
    found = 0
    g_loc = 0
    for i in range(len(sequence)-3):
        if (sequence[i]== nt) and (sequence[i+1]== nt) and (sequence[i+2]==nt) and (sequence[i+3]==nt) :
            found += 1
            g_loc = i
            
    if found != 1 :
        return -1
    else:
        return (g_loc + 1)

def ProbeSetWithGstack(filename, outputFile = ""):
    listOfProbeSet = list()
    with open(filename, mode='r') as tempFile:
        for line in tempFile:
            *_, probeSetId = line.split()
            listOfProbeSet.append(probeSetId)
            
    setOfProbeSet = set(listOfProbeSet)
    if outputFile != "":
        with open(outputFile, mode='a', encoding="utf-8") as outFile:
            for item in setOfProbeSet:
                outFile.write(item)

    return len(setOfProbeSet)
        


