# anagram

def anagram(first, second):
    strings = {}
    strings2 = {}
    for x in first:
        if x in strings:
            strings[x] += 1
        else:
            strings[x] = 1
    for x in second:
        if x in strings2:
            strings2[x] += 1
        else:
            strings2[x] = 1

    return strings == strings2


first = input("1st word: ")
second = input("2nd word: ")
print(f"1st and 2nd words palindrom? {anagram(first, second)}")

