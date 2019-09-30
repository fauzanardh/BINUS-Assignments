prices = {
    "banana": [4, 3],
    "apple": [2, 2],
    "orange": [1.5, 4],
    "pear": [3, 5]
}

total = 0
for x, y in prices.items():
    print(f"{x}\nprice: {y[0]}\nstock: {y[1]}")
    total += y[0]*y[1]

print(total)
