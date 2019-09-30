# count character

def count1(message):
    strings = {}
    for x in z:
        if x in strings:
            strings[x] += 1
        else:
            strings[x] = 1
    for data in strings:
        print(f"{data} = {strings[data]}")

z = input("Message?: ")
print(count1(z))
