def findVal(mydict, value):
    dictFound = []
    for key, val in mydict.items():
        if val == value:
            dictFound.append(key)
    return dictFound


print(findVal({'123': 123, '321': 123, '456': 456}, 123))
