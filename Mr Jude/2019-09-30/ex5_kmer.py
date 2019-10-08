import pprint


def count(string):
    returnDict = {}
    for char in string:
        returnDict[char] = returnDict.get(char, 0) + 1
    return returnDict


def makeKMER(DNAString, k):
    splitted = list(DNAString)
    returnDict = {}
    for i in range(k, 0, -1):
        returnDict[i] = {}
        returnDict[i]["kmer"] = []
        returnDict[i]["kmerCount"] = []
        for x in range(len(splitted)-(i-1)):
            kmer = "".join([splitted[x+z-1] for z in range(i)])
            returnDict[i]["kmer"].append(kmer)
            returnDict[i]["kmerCount"].append(count(kmer))

    pprint.pprint(returnDict)


makeKMER("GTAGAGCTGT", 10)
