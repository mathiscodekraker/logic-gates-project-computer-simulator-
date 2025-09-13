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

def ConvertSymbolToBinary(Sybmol):
    return

def ConvertStringToBinary(StringValue):
    return
