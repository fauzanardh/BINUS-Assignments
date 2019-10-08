users = {
    "admin": "123"
}


def acceptLogin(users, username, password):
    return users.get(username, -1) == password


username = input("Enter your username: ")
password = input("Enter your password: ")
if acceptLogin(users, username, password):
    print("Ayy you did it, you logged in lol")
else:
    print("Who are you? i don't know you, shoo shoo")
