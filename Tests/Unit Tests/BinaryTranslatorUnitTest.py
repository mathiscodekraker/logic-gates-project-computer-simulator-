#librarys
import BasicUnitTest as UT

#specific unit test
def ConvertBinaryStringToBoolListUnitTest():
    UT.BasicUnitTestExecution("ConvertBinaryStringToBoolList")
    pass

def ConvertBoolListToBinaryUnitTest():
    UT.BasicUnitTestExecution("ConvertBoolListToBinary")
    pass

def ConvertSymbolToBinaryUnitTest():
    UT.BasicUnitTestExecution("ConvertSymbolToBinary")
    pass

def ConvertBinaryToSymbolUnitTest():
    UT.BasicUnitTestExecution("ConvertBinaryToSymbol")
    pass

def ConvertStringToBinaryUnitTest():
    UT.BasicUnitTestExecution("ConvertStringToBinary")
    pass

def ConvertIntToBinarySpecificSizeUnitTest():
    UT.BasicUnitTestExecution("ConvertIntToBinarySpecificSize", True)
    pass

def ConvertIntToBinaryUnitTest():
    UT.BasicUnitTestExecution("ConvertIntToBinary")
    pass

def ConvertBinaryToIntUnitTest():
    UT.BasicUnitTestExecution("ConvertBinaryToInt")
    pass

#execute tests
ConvertBinaryStringToBoolListUnitTest()
ConvertBoolListToBinaryUnitTest()
ConvertBinaryToIntUnitTest()
ConvertIntToBinaryUnitTest()
ConvertIntToBinarySpecificSizeUnitTest()
ConvertSymbolToBinaryUnitTest()
ConvertBinaryToSymbolUnitTest()
ConvertStringToBinaryUnitTest()

