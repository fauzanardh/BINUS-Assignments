# simple hangman

from random import choice
from re import sub


def replaceToChar(sentence, guessed, char):
    indexes = []
    for x in range(len(sentence)):
        if char.lower() == sentence[x].lower():
            indexes.append(x)
    if not indexes:
        return False, guessed
    for i in indexes:
        guessed = list(guessed)  # changing to list so it becomes muteable
        guessed[i] = sentence[i]
    return True, "".join(guessed)


SENTENCES = ["BINUS University International", "Python Lesson",
             "I will just put anything here", "Ayy Lmao"]  # sentence pool
life = 5
chosen = choice(SENTENCES)  # selecting random sentence from the pool
guessed = sub("[a-zA-Z]", "_", chosen)  # changing every character to _

print("Welcome to hangman!")
while life > 0:
    print(guessed)
    print(f"Your life: {life}")
    guess = input("Your guess? ")
    if len(guess) != 1:
        print("Wrong char length!")
    x, guessed = replaceToChar(chosen, guessed, guess)
    if guessed == chosen:
        print(guessed)
        print("You win!")
        exit()
    if not x:
        print("Your guess is wrong!")
        life -= 1
print("You lose!")
