import re

words = {}

for y in re.findall("[a-zA-Z]+", input("Enter some words\n> ")):
    words[y] = words.get(y, 0) + 1

print(words)
