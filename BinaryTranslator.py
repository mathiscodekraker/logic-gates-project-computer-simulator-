#librarys
import math

#variables
SymbolToIntValueDictionary = {
    "0": 48, "1": 49, "2": 50, "3": 51, "4": 52,
    "5": 53, "6": 54, "7": 55, "8": 56, "9": 57,

    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69,
    "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
    "K": 75, "L": 76, "M": 77, "N": 78, "O": 79,
    "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90,

    "a": 97, "b": 98, "c": 99, "d": 100, "e": 101,
    "f": 102, "g": 103, "h": 104, "i": 105, "j": 106,
    "k": 107, "l": 108, "m": 109, "n": 110, "o": 111,
    "p": 112, "q": 113, "r": 114, "s": 115, "t": 116,
    "u": 117, "v": 118, "w": 119, "x": 120, "y": 121, "z": 122,

    ".": 46, ",": 44, "!": 33, "?": 63, "'": 39,
    "(": 40, ")": 41, "-": 45, "\"": 34, " ": 32
}
IntToSymbolValueDictionary = {v: k for k, v in SymbolToIntValueDictionary.items()}

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
    ReverseBinaryString = ReverseBinaryString.replace(" ", "")
    BitValue = 1
    Output = 0
    for each in ReverseBinaryString:
        if each == "1":
            Output += BitValue
            pass
        BitValue = BitValue * 2
        pass
    return Output

def ConvertIntToBinary(IntInput):
    #get log of 2^n = IntInput and then round up
    n = math.ceil(math.log2(IntInput + 1))
    index = 0
    OutputString = ""
    while 0 < n:
        if (IntInput - (2 ** (n-1))) >= 0:
            IntInput -= (2 ** (n-1))
            OutputString += "1"
        else:
            OutputString += "0"
            pass
        n -= 1
        pass

    if OutputString == "":
        OutputString = "0"
        pass
    return OutputString

def ConvertIntToBinarySpecificSize(IntInput, BitStringSize):
    BinaryString = ConvertIntToBinary(IntInput)
    StringLen = len(BinaryString)
    StringLenDifference = BitStringSize - StringLen
    if StringLenDifference > 0:
        BinaryString = "0"*StringLenDifference + BinaryString
        pass
    return BinaryString

def ConvertSymbolToBinary(Symbol):
    IntInput = SymbolToIntValueDictionary[Symbol]
    return ConvertIntToBinarySpecificSize(IntInput, 7)

def ConvertBinaryToSymbol(BinaryString):
    IntValue = ConvertBinaryToInt(BinaryString)
    return IntToSymbolValueDictionary[IntValue]

def ConvertStringToBinary(StringValue):
    BinaryList = []
    for EachSymbol in StringValue:
        BinaryList.append(ConvertSymbolToBinary(EachSymbol))
        pass
    return BinaryList
