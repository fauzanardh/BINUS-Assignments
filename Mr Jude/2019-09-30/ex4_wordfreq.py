import re


def wordFreq(words):
    word_count = {}
    for y in re.findall("[a-zA-Z]+", words):
        word_count[y] = word_count.get(y, 0) + 1
    return word_count


print(wordFreq("Calvin is gay, like really gay. JK he's not gay OwO"))
