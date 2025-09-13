#Library
import BasicLogicGates as BLG
import LogicGateCombinations as LGC

#functions
#basic logic gates
def NAND(InputsForEachBitList, BitstringSize):
    OutputsForEachBitList = []
    index = 0
    while index < BitstringSize:
        each = InputsForEachBitList[index]
        BitOutput = [BLG.NAND(each[0], each[1])]
        OutputsForEachBitList.append(BitOutput)
        index += 1
        pass
    return OutputsForEachBitList

#logic gate combinations


