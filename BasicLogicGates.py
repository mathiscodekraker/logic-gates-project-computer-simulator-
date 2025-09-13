#gates
#NAND 00=1, 01=1, 10=1, 11=0
def NAND(Input1, Input2):
    if Input1 and Input2:
        return False
    else:
        return True
    pass

#NOT 0=1, 1=0
def NOT(Input1):
    return NAND(Input1, Input1)

#AND 00=0, 01=0, 10=0, 11=1
def AND(Input1, Input2):
    return NOT(NAND(Input1, Input2))

#OR 00=0, 01=1, 10=1, 11=1
def OR(Input1, Input2):
    return NAND(NOT(Input1), NOT(Input2))

#XOR 00=0, 01=1, 10=1, 11=0
def XOR(Input1, Input2):
    return AND(NAND(Input1, Input2), OR(Input1, Input2))
