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

print(IntToSymbolValueDictionary)

print(2, ConvertBinaryToInt("010"))
print(4, ConvertBinaryToInt("0100"))
print(5, ConvertBinaryToInt("0101"))
print(8, ConvertIntToBinary(8))
print(200, ConvertIntToBinary(200))
print(0, ConvertIntToBinary(0))
print(20, ConvertIntToBinary(20))
print(2, ConvertIntToBinary(2))
print(1, ConvertIntToBinary(1))
print(3, ConvertIntToBinary(3))

print(8, "4bits", ConvertIntToBinarySpecificSize(8, 4))
print(200, "2bits", ConvertIntToBinarySpecificSize(200, 2))
print(0, "8bits", ConvertIntToBinarySpecificSize(0, 8))
print(20, "8bits", ConvertIntToBinarySpecificSize(20, 8))
print(2, "7bits",ConvertIntToBinarySpecificSize(2, 7))
print(1, "6bits", ConvertIntToBinarySpecificSize(1, 6))
print(3, "5bits", ConvertIntToBinarySpecificSize(3, 5))

print(ConvertStringToBinary("H!"))
print(ConvertStringToBinary("HaSs!"))
print(ConvertStringToBinary("3425"))

print("0", ConvertBinaryToSymbol("0110000"))
print("!", ConvertBinaryToSymbol("010 0001"))
print("?", ConvertBinaryToSymbol("011 1111"))

print("7", ConvertBinaryToSymbol("011 0111"))
print("H", ConvertBinaryToSymbol("100 1000"))
print("U", ConvertBinaryToSymbol("101 0101"))
print("h", ConvertBinaryToSymbol("110 1000"))
print("u", ConvertBinaryToSymbol("111 0101"))
print("spatie." + ConvertBinaryToSymbol("010 0000") + ".")
