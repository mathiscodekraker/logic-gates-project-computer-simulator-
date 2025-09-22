List1 = []
List2 = []

def GetListLen(VarName):
    return len(globals()[VarName])

def ConvertBinaryStringToBoolListTestDataSet():
    global List1, List2
    TestInputsList = ["01110", "h", "h01", "0"]
    List1 = TestInputsList
    ExpectedOutputs = [[False, True, True, True, False], "ERROR", "ERROR", [False]]
    List2 = ExpectedOutputs
    pass

def ConvertBinaryStringToBoolListTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]

def ConvertBoolListToBinaryTestDataSet():
    global List1, List2
    TestInputsList = [[False, True], [True, True, False, True, False, False, False], [False], [False, True, True, True, False]]
    List1 = TestInputsList
    ExpectedOutputs = ["01", "1101000", "0", "01110"]
    List2 = ExpectedOutputs
    pass

def ConvertBoolListToBinaryTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]

#####################################
def ConvertSymbolToBinaryTestDataSet():
    global List1, List2
    TestInputsList = ["0", "!", "?", "7", "H", "U", "h", "u", " "]
    List1 = TestInputsList
    ExpectedOutputs = ["0110000", "0100001", "0111111", "0110111", "1001000", "1010101", "1101000", "1110101", "0100000"]
    List2 = ExpectedOutputs
    pass

def ConvertSymbolToBinaryTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]

def ConvertBinaryToSymbolTestDataSet():
    global List1, List2
    TestInputsList = ["0110000", "0100001", "0111111", "0110111", "1001000", "1010101", "1101000", "1110101", "0100000"]
    List1 = TestInputsList
    ExpectedOutputs = ["0", "!", "?", "7", "H", "U", "h", "u", " "]
    List2 = ExpectedOutputs
    pass

def ConvertBinaryToSymbolTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]

def ConvertStringToBinaryTestDataSet():
    global List1, List2
    TestInputsList = ["H!", "HaSs!", "3425"]
    List1 = TestInputsList
    ExpectedOutputs = [['1001000', '0100001'], ['1001000', '1100001', '1010011', '1110011', '0100001'], ['0110011', '0110100', '0110010', '0110101']]
    List2 = ExpectedOutputs
    pass

def ConvertStringToBinaryTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]

def ConvertIntToBinarySpecificSizeTestDataSet():
    global List1, List2
    TestInputsList = [[8, 4], [200, 2], [0, 8], [20, 8], [2, 7], [1, 6], [3, 5]]
    List1 = TestInputsList
    ExpectedOutputs = ['1000', '11001000', '00000000', '00010100', '0000010', '000001', '00011']
    List2 = ExpectedOutputs
    pass

def ConvertIntToBinarySpecificSizeTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]

def ConvertIntToBinaryTestDataSet():
    global List1, List2
    TestInputsList = [8, 200, 0, 20, 2, 1, 3]
    List1 = TestInputsList
    ExpectedOutputs = ['1000', '11001000', '0', '10100', '10', '1', '11']
    List2 = ExpectedOutputs
    pass

def ConvertIntToBinaryTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]

def ConvertBinaryToIntTestDataSet():
    global List1, List2
    TestInputsList = ["010", "0100", "0101"]
    List1 = TestInputsList
    ExpectedOutputs = [2, 4, 5]
    List2 = ExpectedOutputs
    pass

def ConvertBinaryToIntTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]


