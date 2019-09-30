def findVal(mydict, val):
    dictFound = []
    for x, y in mydict.items():
        if y == val:
            dictFound.append(x)
    return dictFound


print(findVal({'123': 123, '321': 123, '456': 456}, 123))
