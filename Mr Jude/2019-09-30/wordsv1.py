words = {}
x = input("Enter some words\n> ")
for y in x.split(" "):
    words[y] = words.get(y, 0) + 1

print(words)
