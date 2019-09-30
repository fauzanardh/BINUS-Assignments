foodlist = ["banana", "banana", "orange", "apple"]

stock = {
    "banana": 2,
    "apple": 1,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def computeBill(food):
    total = 0
    for f in food:
        if stock[f] > 0:
            total += prices[f]
            stock[f] -= 1
    return total


print(computeBill(foodlist))
