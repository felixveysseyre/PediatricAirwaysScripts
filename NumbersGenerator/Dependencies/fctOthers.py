# General imports



# Class imports



# Function import



# Function definition

def displayList(list):
    for i in range(len(list)):
        print(list[i])

def createListFromListFile(inputsFilePath):
    inputsFile = open(inputsFilePath)
    inputsList = []

    for lineTemp in inputsFile:
        inputsList.append(lineTemp)

    inputsFile.close()

    inputsList = map(lambda s: s.strip(), inputsList) #clean the \n

    return inputsList