ComputerInput = input("Input your chosen computer (circuit design) here: ")
CodeInput = input("Input your chosen code file (asambly languague) to execute on the computer here: ")

#variables
#memory bits
#naming conventions (versie van dit soort gates in nummers 1, 2, 3, ...)
MemoryBitsDictionary = {}

#where the outputs for each gate go
#naming conventions (if it is a output = O or input = I if input kan bijv. I1 of I2 zijn)(naam soort bit bijv. M, NAND, OR, AND, etc.)(versie van dit soort gate in nummers 1, 2, 3, ...)
#dictionary value is een list met al de richtingen waar de output in gaat
WhereTheOutputGoesToDictionary = {}

LastInputDictionary = {}
InputsListsListOrganised = []
#when LastOutputDictionary is completed LastInputDictionary = LastOutputDictionary
LastOutputDictionary = {}
