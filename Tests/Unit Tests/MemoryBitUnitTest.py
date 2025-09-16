#librarys
import os
import sys
CurrentDirectory = os.path.dirname(os.path.abspath(__file__))
MainDirectory = CurrentDirectory[:(len(CurrentDirectory) - len(r"\Tests\Unit Tests"))]
sys.path.append(MainDirectory)
import MemoryBit as MB
sys.path.append(MainDirectory + "\Tests\Test Data")
import MemoryBitUnitTestTestData as TD

#unit tests
def ReadOutputUnitTest():
    print("ReadOutput unit test for all possible ways you can create a memory bit: ")

    TD.ReadOutputTestDataSet()
    AllUnitTestsWereSuccessful = True
    AmountOfUnitTests = TD.GetListLen("List1")
    VersionOfUnitTest = 0
    while VersionOfUnitTest < AmountOfUnitTests:
        TestInputs, ExpectedOutput = TD.ReadOutputTestData(VersionOfUnitTest)
        M = MB.MemoryBit(TestInputs)
        if not ExpectedOutput == M.ReadOutput():
            AllUnitTestsWereSuccessful = False
            print("False")
        else:
            print("True")
            pass
        VersionOfUnitTest += 1
        pass
    print("All unit tests were true = " + str(AllUnitTestsWereSuccessful))
    pass

def UpdateMemoryBitUnitTest():
    print("UpdateMemoryBit unit test for all possible ways you can create a memory bit: ")

    TD.UpdateMemoryBitTestDataSet()
    AllUnitTestsWereSuccessful = True
    AmountOfUnitTests = TD.GetListLen("List1")
    VersionOfUnitTest = 0
    while VersionOfUnitTest < AmountOfUnitTests:
        AmountOfUnitTestsInTheUnitTests = TD.GetListLen("List2")
        VersionOfInternalUnitTest = 0
        while VersionOfInternalUnitTest < AmountOfUnitTestsInTheUnitTests:
            SetOriginalTestState, TestInputInternal, ExpectedOutput = TD.UpdateMemoryBitTestData(VersionOfUnitTest, VersionOfInternalUnitTest)
            M = MB.MemoryBit(SetOriginalTestState)
            Output = M.UpdateMemoryBit(TestInputInternal[0], TestInputInternal[1])
            if not ExpectedOutput == Output:
                AllUnitTestsWereSuccessful = False
                print("False")
            else:
                print("True")
                pass
            VersionOfInternalUnitTest += 1
            pass
        VersionOfUnitTest += 1
        pass
    print("All unit tests were true = " + str(AllUnitTestsWereSuccessful))
    pass

ReadOutputUnitTest()
UpdateMemoryBitUnitTest()
