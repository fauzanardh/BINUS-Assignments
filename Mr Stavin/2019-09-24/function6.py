# anagraom w/o using sorted or dictionary

def isAnagram(first, second):
    if len(first) == len(second):
        for element in first:
            if element in second:
                second = second.replace(element, "", 1)
            else:
                return False
        return True
    return False


print(isAnagram("michael", "limache"))
print(isAnagram("woaa", "wooa"))