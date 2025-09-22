#librarys
import os
import sys
CurrentDirectory = os.path.dirname(os.path.abspath(__file__))
MainDirectory = CurrentDirectory[:(len(CurrentDirectory) - len(r"\Tests\Unit Tests"))]
sys.path.append(MainDirectory)
import BinaryTranslator as Code
sys.path.append(MainDirectory + "\Tests\Test Data")
import BinaryTranslatorUnitTestTestData as TD

#unit tests
#basic unit test
def BasicUnitTest(TestedFunctionName, UnitTestVersionIndex, MultipleInputs=False):
    Input, ExpectedOutput = getattr(TD, TestedFunctionName + "TestData")(UnitTestVersionIndex)
    if MultipleInputs:
        Output = getattr(Code, TestedFunctionName)(*Input)
    else:
        Output = getattr(Code, TestedFunctionName)(Input)
        pass
    
    if (Output == ExpectedOutput):
        return True
    return False

def BasicUnitTestExecution(TestedFunctionName, MultipleInputs=False):
    index = 0
    getattr(TD, TestedFunctionName + "TestDataSet")()
    AmountOfUnitTests = TD.GetListLen("List1")
    AllUnitTestsWereSuccessful = True
    print(TestedFunctionName + ": ")
    while index < AmountOfUnitTests:
        if MultipleInputs:
            OutputUnitTest = BasicUnitTest(TestedFunctionName, index, True)
        else:
            OutputUnitTest = BasicUnitTest(TestedFunctionName, index)
            pass
        
        print(OutputUnitTest)
        index += 1
        if not OutputUnitTest:
            AllUnitTestsWereSuccessful = False
            pass
        pass
    print("All UnitTests Were Successful: " + str(AllUnitTestsWereSuccessful))
    print("")
    pass
