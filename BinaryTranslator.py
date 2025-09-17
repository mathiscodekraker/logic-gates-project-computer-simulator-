#librarys
import math

#variables
SymbolToIntValueDictionary = { "example a": 1 }
IntToSymbolValueDictionary = {v: k for k, v in my_dict.items()}

#functions
def ConvertBinaryStringToBoolList(BinaryString):
    BoolList = []
    for each in BinaryString:
        if each == "1":
            BoolList.append(True)
        elif each == "0":
            BoolList.append(False)
        else:
            return "ERROR"
        pass
    return BoolList

def ConvertBoolListToBinary(BoolList):
    Binary = []
    for each in BoolList:
        if each:
            Binary.append("1")
        else:
            Binary.append("0")
        pass
    BinaryString = "".join(Binary)
    return BinaryString

#convert binary to int 
def ConvertBinaryToInt(BinaryString):
    ReverseBinaryString = BinaryString[::-1]
    BitValue = 1
    Output = 0
    for each in BinaryString:
        if each == 1:
            Output += BitValue
            pass
        BitValue = BitValue * 2
        pass
    return Output

def ConvertIntToBinary(IntInput):
    #get log of 2^n = IntInput and then round up
    n = math.ceil(math.log2(intvalue + 1))
    index = 0
    OutputString = ""
    while 0 < n:
        if (IntInput - (2 ** n)) > 0:
            IntInput -= (2 ** n)
            OutputString += "1"
        else:
            OutputString += "0"
            pass
        n -= 1
        pass
    if IntInput == 1:
        OutputString[:-len("0")]
        OutputString += "1"
        pass
    return OutputString

def ConvertSymbolToBinary(Sybmol):
    IntInput = SymbolToIntValueDictionary["Symbol"]
    return ConvertIntToBinary(IntInput)

def ConvertBinaryToSymbol(BinaryString):
    return

def ConvertStringToBinary(StringValue):
    return
