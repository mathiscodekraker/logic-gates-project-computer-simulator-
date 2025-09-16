#Library
import BasicLogicGates as BLG
import LogicGateCombinations as LGC

#functions
def GiveLengthList(Input1, Input2):
    if isinstance(Input1, list) and isinstance(Input2, list):
        if len(Input1) == len(Input2):
            return len(Input1)
            pass
    elif isinstance(Input1, list):
        return len(Input1)
    elif isinstance(Input2, list):
        return len(Input2)
    return "Error"

def ConvertInputsToList(Input1ForEachBit, Input2ForEachBit):
    if not isinstance(Input1ForEachBit, list):
        Input1ForEachBit = [Input1ForEachBit] * BitstringSize
        pass
    if not isinstance(Input2ForEachBit, list):
        Input2ForEachBit = [Input2ForEachBit] * BitstringSize
        pass
    return Input1ForEachBit, Input2ForEachBit

#basic logic gates
def NAND(Input1ForEachBit, Input2ForEachBit):
    BitstringSize = GiveLengthList(Input1ForEachBit, Input2ForEachBit)
    Input1ForEachBit, Input2ForEachBit = ConvertInputsToList(Input1ForEachBit, Input2ForEachBit)
    
    OutputsForEachBitList = []
    index = 0
    while index < BitstringSize:
        BitOutput = BLG.NAND(Input1ForEachBit[index], Input2ForEachBit[index])
        OutputsForEachBitList.append(BitOutput)
        index += 1
        pass
    return OutputsForEachBitList

def NOT(Input1ForEachBit):
    BitstringSize = len(Input1ForEachBit)
    OutputsForEachBitList = []
    index = 0
    while index < BitstringSize:
        BitOutput = BLG.NOT(Input1ForEachBit[index])
        OutputsForEachBitList.append(BitOutput)
        index += 1
        pass
    return OutputsForEachBitList

def AND(Input1ForEachBit, Input2ForEachBit):
    BitstringSize = GiveLengthList(Input1ForEachBit, Input2ForEachBit)
    Input1ForEachBit, Input2ForEachBit = ConvertInputsToList(Input1ForEachBit, Input2ForEachBit)
    
    OutputsForEachBitList = []
    index = 0
    while index < BitstringSize:
        BitOutput = BLG.AND(Input1ForEachBit[index], Input2ForEachBit[index])
        OutputsForEachBitList.append(BitOutput)
        index += 1
        pass
    return OutputsForEachBitList

def OR(Input1ForEachBit, Input2ForEachBit):
    BitstringSize = GiveLengthList(Input1ForEachBit, Input2ForEachBit)
    Input1ForEachBit, Input2ForEachBit = ConvertInputsToList(Input1ForEachBit, Input2ForEachBit)
    
    OutputsForEachBitList = []
    index = 0
    while index < BitstringSize:
        BitOutput = BLG.OR(Input1ForEachBit[index], Input2ForEachBit[index])
        OutputsForEachBitList.append(BitOutput)
        index += 1
        pass
    return OutputsForEachBitList

def XOR(Input1ForEachBit, Input2ForEachBit):
    BitstringSize = GiveLengthList(Input1ForEachBit, Input2ForEachBit)
    Input1ForEachBit, Input2ForEachBit = ConvertInputsToList(Input1ForEachBit, Input2ForEachBit)
    
    OutputsForEachBitList = []
    index = 0
    while index < BitstringSize:
        BitOutput = BLG.XOR(Input1ForEachBit[index], Input2ForEachBit[index])
        OutputsForEachBitList.append(BitOutput)
        index += 1
        pass
    return OutputsForEachBitList

#logic gate combinations


