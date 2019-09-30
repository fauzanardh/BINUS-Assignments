users = {
    "admin": "123"
}


def acceptLogin(users, username, password):
    if username in users:
        if users[username] == password:
            return True
    return False


username = input("Enter your username: ")
password = input("Enter your password: ")
if acceptLogin(users, username, password):
    print("Ayy you did it, you logged in lol")
else:
    print("Who are you? i don't know you, shoo shoo")
