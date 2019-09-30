def removeKeys(mydict, keylist):
    for key in keylist:
        del mydict[key]


x = {"a": 1, "b": 2}
print(x)
removeKeys(x, ["a", "b"])
print(x)
