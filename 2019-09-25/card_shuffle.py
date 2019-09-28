# card shuffle

from random import shuffle

def initializeCards():
    cards = []
    for x in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
        for y in ["Spade", "Heart", "Diamond", "Club"]:
            cards.append((y, x))
    return cards

cards = initializeCards()
print("First 5 cards:")
for card in cards[0:5]: print(f"{card[1]} of {card[0]}", end=", ")
print("\nShuffling...")
shuffle(cards)
print("First 5 cards after shuffled:")
for card in cards[0:5]: print(f"{card[1]} of {card[0]}", end=", ")