#librarys
import os
import sys
CurrentDirectory = os.path.dirname(os.path.abspath(__file__))
MainDirectory = CurrentDirectory[:(len(CurrentDirectory) - len(r"\Tests\Unit Tests"))]
sys.path.append(MainDirectory)
import BasicLogicGates as BLG
sys.path.append(MainDirectory + "\Tests\Test Data")
import BasicLogicGatesUnitTestTestData as TD

def NANDUnitTest():
    print("NAND unit test for all possible ways you can create a memory bit: ")

    TD.NANDTestDataSet()
    AllUnitTestsWereSuccessful = True
    AmountOfUnitTests = TD.GetListLen("List1")
    VersionOfUnitTest = 0
    while VersionOfUnitTest < AmountOfUnitTests:
        TestInputs, ExpectedOutput = TD.NANDTestData(VersionOfUnitTest)
        ResultOutput = BLG.NAND(TestInputs[0], TestInputs[1])
        if not ExpectedOutput == ResultOutput:
            AllUnitTestsWereSuccessful = False
            print("False")
        else:
            print("True")
            pass
        VersionOfUnitTest += 1
        pass
    print("All unit tests were true = " + str(AllUnitTestsWereSuccessful))
    pass

def NOTUnitTest():
    print("NOT unit test for all possible ways you can create a memory bit: ")

    TD.NOTTestDataSet()
    AllUnitTestsWereSuccessful = True
    AmountOfUnitTests = TD.GetListLen("List1")
    VersionOfUnitTest = 0
    while VersionOfUnitTest < AmountOfUnitTests:
        TestInputs, ExpectedOutput = TD.NOTTestData(VersionOfUnitTest)
        ResultOutput = BLG.NOT(TestInputs)
        if not ExpectedOutput == ResultOutput:
            AllUnitTestsWereSuccessful = False
            print("False")
        else:
            print("True")
            pass
        VersionOfUnitTest += 1
        pass
    print("All unit tests were true = " + str(AllUnitTestsWereSuccessful))
    pass

def ANDUnitTest():
    print("AND unit test for all possible ways you can create a memory bit: ")

    TD.ANDTestDataSet()
    AllUnitTestsWereSuccessful = True
    AmountOfUnitTests = TD.GetListLen("List1")
    VersionOfUnitTest = 0
    while VersionOfUnitTest < AmountOfUnitTests:
        TestInputs, ExpectedOutput = TD.ANDTestData(VersionOfUnitTest)
        ResultOutput = BLG.AND(TestInputs[0], TestInputs[1])
        if not ExpectedOutput == ResultOutput:
            AllUnitTestsWereSuccessful = False
            print("False")
        else:
            print("True")
            pass
        VersionOfUnitTest += 1
        pass
    print("All unit tests were true = " + str(AllUnitTestsWereSuccessful))
    pass

def ORUnitTest():
    print("OR unit test for all possible ways you can create a memory bit: ")

    TD.ORTestDataSet()
    AllUnitTestsWereSuccessful = True
    AmountOfUnitTests = TD.GetListLen("List1")
    VersionOfUnitTest = 0
    while VersionOfUnitTest < AmountOfUnitTests:
        TestInputs, ExpectedOutput = TD.ORTestData(VersionOfUnitTest)
        ResultOutput = BLG.OR(TestInputs[0], TestInputs[1])
        if not ExpectedOutput == ResultOutput:
            AllUnitTestsWereSuccessful = False
            print("False")
        else:
            print("True")
            pass
        VersionOfUnitTest += 1
        pass
    print("All unit tests were true = " + str(AllUnitTestsWereSuccessful))
    pass

def XORUnitTest():
    print("XOR unit test for all possible ways you can create a memory bit: ")

    TD.XORTestDataSet()
    AllUnitTestsWereSuccessful = True
    AmountOfUnitTests = TD.GetListLen("List1")
    VersionOfUnitTest = 0
    while VersionOfUnitTest < AmountOfUnitTests:
        TestInputs, ExpectedOutput = TD.XORTestData(VersionOfUnitTest)
        ResultOutput = BLG.XOR(TestInputs[0], TestInputs[1])
        if not ExpectedOutput == ResultOutput:
            AllUnitTestsWereSuccessful = False
            print("False")
        else:
            print("True")
            pass
        VersionOfUnitTest += 1
        pass
    print("All unit tests were true = " + str(AllUnitTestsWereSuccessful))
    pass

NANDUnitTest()
NOTUnitTest()
ANDUnitTest()
ORUnitTest()
XORUnitTest()
