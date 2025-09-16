List1 = []
List2 = []

def GetListLen(VarName):
    return len(globals()[VarName])

def NANDTestDataSet():
    global List1, List2
    TestInputsList = [[0, 0], [0, 1], [1, 0], [1, 1]]
    List1 = TestInputsList
    ExpectedOutputs = [1, 1, 1, 0]
    List2 = ExpectedOutputs
    pass

def NANDTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]

def NOTTestDataSet():
    global List1, List2
    TestInputsList = [0, 1]
    List1 = TestInputsList
    ExpectedOutputs = [1, 0]
    List2 = ExpectedOutputs
    pass

def NOTTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]

def ANDTestDataSet():
    global List1, List2
    TestInputsList = [[0, 0], [0, 1], [1, 0], [1, 1]]
    List1 = TestInputsList
    ExpectedOutputs = [0, 0, 0, 1]
    List2 = ExpectedOutputs
    pass

def ANDTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]

def ORTestDataSet():
    global List1, List2
    TestInputsList = [[0, 0], [0, 1], [1, 0], [1, 1]]
    List1 = TestInputsList
    ExpectedOutputs = [0, 1, 1, 1]
    List2 = ExpectedOutputs
    pass

def ORTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]

def XORTestDataSet():
    global List1, List2
    TestInputsList = [[0, 0], [0, 1], [1, 0], [1, 1]]
    List1 = TestInputsList
    ExpectedOutputs = [0, 1, 1, 0]
    List2 = ExpectedOutputs
    pass

def XORTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]
