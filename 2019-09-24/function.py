# simple calculator

# -*- coding:utf-8 -*-
from functools import reduce

x = []
operation = {
    "ADD": lambda x: reduce(lambda a, b: a+b, x),
    "SUB": lambda x: reduce(lambda a, b: a-b, x),
    "MUL": lambda x: reduce(lambda a, b: a*b, x),
    "DIV": lambda x: reduce(lambda a, b: a/b, x),
}

while True:
    try:
        x.append(eval(input("Enter a number (ctrl+c to continue to the operation): ")))
    except KeyboardInterrupt:
        print(f"\nYour number are {x}")
        break

while True:
    z = input("what operation (ADD, SUB, MUL, DIV)? ")
    try:
        print(f"The result is: {operation[z.upper()](x)}")
        break
    except TypeError:
        print("No result!")
        break
    except KeyError:
        print(f"No operation called {z}")
        continue