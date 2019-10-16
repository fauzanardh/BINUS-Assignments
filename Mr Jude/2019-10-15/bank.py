import json
import hashlib
import random
import atexit
import os

bank = None
username = None


class Account(object):
    def __init__(self, balance):
        self.__balance = balance

    def __str__(self):
        return f"Account(balance={self.getBalance()})"

    def __repl__(self):
        return f"Account(balance={self.getBalance()})"

    def withdraw(self, amount):
        if type(amount) not in [float, int] or amount <= 0 or amount >= self.__balance:
            return False
        self.__balance -= amount
        return True

    def deposit(self, amount):
        if type(amount) not in [float, int] or amount <= 0:
            return False
        self.__balance += amount
        return True

    def getBalance(self):
        return self.__balance


class Customer(object):
    def __init__(self, firstName, lastName, passwordHash, amountOrClassAccount):
        if type(amountOrClassAccount) == int:
            amountOrClassAccount = Account(amountOrClassAccount)
        self.__account = amountOrClassAccount
        self.firstName = firstName
        self.lastName = lastName
        self.passwordHash = passwordHash

    def __str__(self):
        return f"Customer(firstName={self.firstName}, lastName={self.lastName}, balance={self.__account.getBalance()})"

    def __repl__(self):
        return f"Customer(firstName={self.firstName}, lastName={self.lastName}, balance={self.__account.getBalance()})"

    def getFullName(self):
        return self.firstName + self.lastName

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getPasswordHash(self):
        return self.passwordHash

    def isPasswordCorrect(self, password):
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        if self.passwordHash == md5.hexdigest():
            return True
        return False

    def setAccount(self, account):
        self.__account = account

    def getAccount(self):
        return self.__account


class Bank(object):
    def __init__(self, bankName, adminPass):
        self.bankName = bankName
        self.__adminPass = adminPass
        self.__customers = {}

    def addCustomer(self, isClass, username, *data):
        if isClass:
            self.__customers[username] = data[0]
        else:
            self.__customers[username] = Customer(*data)

    def removeCustomer(self, username):
        try:
            del self.__customers[username]
            return True
        except KeyError:
            return False

    def getAdminPass(self):
        return self.__adminPass

    def getBankName(self):
        return self.bankName

    def getNumOfCustomers(self):
        return len(self.__customers)

    def getCustomer(self, username):
        return self.__customers[username]

    def getCustomers(self):
        # copying dict, so it can't be changed outside the class
        return self.__customers.copy()


def loadFromJson(filename):
    global bank
    with open(filename, "r") as fp:
        bankJson = json.load(fp)
    bank = Bank(bankJson["bankName"], bankJson["adminPass"])
    for username, customer in bankJson["customers"].items():
        bank.addCustomer(
            False,
            username,
            customer["firstName"],
            customer["lastName"],
            customer["passwordHash"],
            customer["account"]["balance"],
        )


def saveToJson(filename):
    global bank
    print("saving to json")
    bankJson = {}
    bankJson["bankName"] = bank.bankName
    bankJson["adminPass"] = bank.getAdminPass()
    bankJson["customers"] = {}
    for username, customer in bank.getCustomers().items():
        bankJson["customers"][username] = {
            "account": {"balance": customer.getAccount().getBalance()},
            "firstName": customer.getFirstName(),
            "lastName": customer.getLastName(),
            "passwordHash": customer.getPasswordHash(),
        }
    with open(filename, "w") as fp:
        json.dump(bankJson, fp, indent=4)


def clearConsole():
    os.system("cls" if os.name == "nt" else "clear")


def adminMenu():
    global bank
    global username
    nextMenu = adminMenu
    while True:
        try:
            print("Admin menu:")
            xInput = int(input("1. Add customer\n2. Exit\nChoice: "))
            if xInput == 1:
                firstName = input("First Name: ")
                lastName = input("Last Name: ")
                username = input("Username: ")
                password = input("Password: ")
                md5 = hashlib.md5()
                md5.update(password.encode("utf-8"))
                password = md5.hexdigest()
                bank.addCustomer(False, username, firstName, username, password, 0)
            elif xInput == 2:
                nextMenu = exit
                break
        except ValueError:
            clearConsole()
    nextMenu()


def guestMenu():
    global bank
    global username
    nextMenu = guestMenu
    while True:
        print(f"Welcome to {bank.getBankName()}")
        try:
            xInput = int(
                input("1. Login to Your Account\n2. Login as admin\n3. Exit\nChoice: ")
            )
            if xInput == 1:
                userpass = input("Enter your username and password (user:pass): ")
                username, password = userpass.split(":")[0:2]
                customers = bank.getCustomers()
                if customers[username].isPasswordCorrect(password):
                    nextMenu = customerMenu
                    break
                else:
                    print("Wrong password!")
            elif xInput == 2:
                nextMenu = adminMenu
                adminpass = input("Admin password: ")
                md5 = hashlib.md5()
                md5.update(adminpass.encode("utf-8"))
                if md5.hexdigest() == bank.getAdminPass():
                    nextMenu = adminMenu
                    break
                else:
                    print("Wrong password!")
            elif xInput == 3:
                nextMenu = exit
                break
        except ValueError:
            clearConsole()
    nextMenu()


def customerMenu():
    global bank
    global username
    nextMenu = customerMenu
    while True:
        print(f"Welcome to {bank.getBankName()}")
        print(f"First Name: {bank.getCustomers()[username].getFirstName()}")
        print(f"Last Name: {bank.getCustomers()[username].getLastName()}")
        print(
            f"Your Balance: {bank.getCustomers()[username].getAccount().getBalance()}"
        )
        try:
            xInput = int(input("1. Withdraw\n2. Deposit\n3. Exit\nChoice: "))
            if xInput == 1:
                amount = int(input("Withdraw amount: "))
                if bank.getCustomers()[username].getAccount().withdraw(amount):
                    print("Withdraw successfully!")
                else:
                    print("Invalid amount")
            elif xInput == 2:
                amount = int(input("Deposit amount: "))
                if bank.getCustomers()[username].getAccount().deposit(amount):
                    print("deposit successfully!")
                else:
                    print("Invalid amount")
            elif xInput == 3:
                nextMenu = exit
                break
        except ValueError:
            clearConsole()
    nextMenu()


atexit.register(saveToJson, "bank.json")
loadFromJson("bank.json")
guestMenu()
