List1 = []
List2 = []
List3 = []

def GetListLen(VarName):
    return len(globals()[VarName])

def ReadOutputTestDataSet():
    global List1, List2
    TestInputsList = [0, 0, 1, 1]
    List1 = TestInputsList
    ExpectedOutputs = [0, 0, 1, 1]
    List2 = ExpectedOutputs
    pass

def ReadOutputTestData(InputValue):
    global List1, List2
    TestInputsList = List1
    ExpectedOutputs = List2
    return TestInputsList[InputValue], ExpectedOutputs[InputValue]

def UpdateMemoryBitTestDataSet():
    global List1, List2, List3
    TestOriginalStatesList = [0, 1]
    List1 = TestOriginalStatesList
    TestInputsList = [[0, 0], [0, 1], [1, 0], [1, 1]]
    List2 = TestInputsList
    ExpectedOutputs = [[0, 0, 0, 1], [1, 0, 1, 1]]
    List3 = ExpectedOutputs
    pass

def UpdateMemoryBitTestData(ExternalTestVersion, InternalTestVersion):
    global List1, List2, List3
    WhatExternalUnitTests = List1
    TestInputsList = List2
    ExpectedOutputs = List3
    return WhatExternalUnitTests[ExternalTestVersion], TestInputsList[InternalTestVersion], ExpectedOutputs[ExternalTestVersion][InternalTestVersion]

