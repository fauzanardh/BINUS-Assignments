import json


def loadFile(inputFile):
    with open(inputFile, "r") as fp:
        return json.loads(fp.read())


def saveFile(outfile, jsonData):
    with open(outfile, "w") as fp:
        fp.write(json.dumps(jsonData, indent=4))


def addTweet(username, tweet):
    tweets["tweets"].append({
        "text": tweet,
        "username": username,
    })
    saveFile("tweet2.json", tweets)


tweets = loadFile("tweet2.json")
availableChoice = ['1', '2', '3', '4']
while True:
    print("1. Print tweet\n2. Add tweet")
    choice = input("> ")
    isSave = False

    if choice not in availableChoice:
        continue
    elif choice == '1':
        for tweet in tweets["tweets"]:
            print(f'{tweet["username"]}:', tweet["text"].replace("\n", " "))
    elif choice == '2':
        username = input("Your username? ")
        text = input("Your text\n> ")
        addTweet(username, text)
    else:
        continue
