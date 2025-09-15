#librarys
import BasicLogicGates as BLG

#memory bit
#1i1s = 1o, 1i0s = No change, 0i0s = No change, 0i,1s = 0o 
class MemoryBit:
    #CRUD
    #Create
    def __init__(self, Output):
        self.Output = Output
        pass
    
    #Read
    def ReadOutput(self):
        return self.Output
    
    #Update
    #I = Input, S = Set (meaning that the memory bit can be changed)
    def UpdateMemoryBit(self, I, S):
        N1 = BLG.NAND(I, S)
        N2 = BLG.NAND(N1, S)
        N4 = BLG.NAND(self.Output, N2)
        N3 = BLG.NAND(N1, N4)
        self.Output = N3
        return self.Output
    pass
