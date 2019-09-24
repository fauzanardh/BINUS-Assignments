# Palindrome checking

str_tocheck = input("Enter your string: ")

def ispalindrome(input_str):
    return (input_str == input_str[::-1])

print(ispalindrome(str_tocheck))

def reverse(string):
    return string[::-1]

print(reverse(str_tocheck))

def calcEven(array):
    i = 0
    for x in array:
        if x % 2 == 0:
            i += x
    return i

print(calcEven([0,3,4,5,6,7,9]))


# Task 1: Create a function to return a reversed string (e.g Input: asda; Output: adsa)
# Task 2: Create a function to print the total of even numbers given an input of a list
# (e.g Input [0,3,4,5,6,7,9] Output 10)