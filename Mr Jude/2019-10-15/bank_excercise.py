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
    def __init__(self, firstName, lastName, amountOrClassAccount):
        if type(amountOrClassAccount) == int:
            amountOrClassAccount = Account(amountOrClassAccount)
        self.__account = amountOrClassAccount
        self.firstName = firstName
        self.lastName = lastName

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

    def setAccount(self, account):
        self.__account = account

    def getAccount(self):
        return self.__account


class Bank(object):
    def __init__(self, bankName):
        self.bankName = bankName
        self.numOfCustomers = 0
        self.__customers = []

    def addCustomer(self, isClass, *data):
        if isClass:
            self.__customers.append(*data)
        else:
            self.__customers.append(Customer(*data))
        self.numOfCustomers += 1

    def removeCustomer(self, index):
        try:
            self.__customers.pop(index)
            self.numOfCustomers -= 1
            return True
        except IndexError:
            return False

    def getBankName(self):
        return self.bankName

    def getNumOfCustomers(self):
        return self.numOfCustomers

    def getCustomer(self, index):
        return self.__customers[index]

    def getCustomers(self):
        return self.__customers


bank = Bank("MyBank")
account1 = Account(1000)
customer1 = Customer("A", "B", account1)
bank.addCustomer(True, customer1)
bank.addCustomer(False, "C", "D", 5000)
print(bank.getBankName())
print(bank.getNumOfCustomers())
print(bank.getCustomer(0))
print(bank.getCustomer(1))
print(bank.getCustomers())
