"""
This is Probe Class modules
"""
from helper import WriteToFile


class Probe():
    """
    Probe Class Provide functionality to create probe object for each probes in sequence. 
    They also provide helper functions too. 

    """
    def __init__(self, probeSetId="", probeX="", probeY="", probeCategory=""):
        self.probeSetId     = probeSetId
        self.probeX         = probeX
        self.probeY         = probeY
        self.probeCategory  = probeCategory

    
    @property
    def probeSetId(self):
        return self.__probeSetId
    
    @probeSetId.setter
    def probeSetId(self, value):
        self.__probeSetId = value
            
    @property
    def probeX(self):
        return self.__probeX
    
    @probeX.setter
    def probeX(self, value):
        self.__probeX = value

    @property
    def probeY(self):
        return self.__probeY
    
    @probeY.setter
    def probeY(self, value):
        self.__probeY = value

    @property
    def probeCategory(self):
        return self.__probeCategory
    
    @probeCategory.setter
    def probeCategory(self, value):
        self.__probeCategory = value



    def WriteProbes(self, path, position=0, combined = False ):
        """ 
        Takes three arguments
        \n1. path to store files 
        \n2. position[optional] to write probe based on its Gstack position
        \n3. combined [optional] bool True to create a combined file of all gstack probes
        """
        outputText = self.__probeX + "\t" + self.__probeY + "\t" + self.__probeSetId +"\n" 
        if position > 0:
            filename = path + "loc" + str(position) + ".txt"
            WriteToFile(filename, outputText)
        if combined:
            filename = path + "combined.txt"
            WriteToFile(filename, outputText)
