import pprint


def makeKMER(DNAString, k):
    splitted = list(DNAString)
    returnDict = {}
    for i in range(k, 0, -1):
        returnDict[i] = []
        for x in range(len(splitted)-(i-1)):
            returnDict[i].append("".join([splitted[x+z-1] for z in range(i)]))
    pprint.pprint(returnDict)


makeKMER("GTAGAGCTGT", 10)
