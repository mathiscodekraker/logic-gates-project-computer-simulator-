#librarys
import BasicLogicGates as BLG

#gate combinations
#memory bit
#I = input, S = Set 
def M(MemoryBitVersion, I, S):
    return MemoryBitVersion.UpdateMemoryBit(I, S)

#register
def R(MemoryBitVersion, I, S, E):
    if E == 0:
        return 0
    else:
        return M(MemoryBitVersion, I, S)
    pass

#and gate combination
def ANDGateCombination(InputList):
    AmountOfInputs = len(InputList)
    if (AmountOfInputs % 2) == 0:
        AndGateInputList = InputList
    else:
        FirstInput = BLG.AND(InputList[0], InputList[1])
        AndGateInputList = InputList
        del AndGateInputList[0]
        del AndGateInputList[1]
        AndGateInputList.insert(0, FirstInput)
        pass

    AndGateOutputList = AndGateInputList
    while len(AndGateOutputList) != 1:
        AmountOfANDGates = len(AndGateOutputList) / 2
        index = 0
        InternalOutputList = []
        while index < AmountOfANDGates:
            InternalOutputList.append(BLG.AND(AndGateOutputList[0], AndGateOutputList[1]))
            del AndGateOutputList[0]
            del AndGateOutputList[1]
            index += 1
            pass
        AndGateOutputList = InternalOutputList
        pass
    return AndGateOutputList[0]

#call upon logic gate combination from txt file
def LogicGateCombinationFromTxtFile(InputsForEachBitList):
    #whatever txt file input functies word 
    return OutputsForEachBitList
