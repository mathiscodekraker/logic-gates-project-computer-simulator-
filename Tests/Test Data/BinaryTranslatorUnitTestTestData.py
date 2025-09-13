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
def ConvertSymbolToBinary(Sybmol):
    return

def ConvertStringToBinary(StringValue):
    return
