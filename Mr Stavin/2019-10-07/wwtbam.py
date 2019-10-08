import random

payouts = [
    10,
    100,
    1000,
    10000,
    100000,
][::-1]

questions = {
    0: {
        "questions": "What was Ally McBeal's profession?",
        "answers": ['Lawyer', 'Accountant', 'Doctor', 'Social Worker'],
        "rightAnswer": 0
    },
    1: {
        "questions": "What word can be put in front of the words 'track', 'way' and 'horse' to make three other words?",
        "answers": ['Road', 'Sound', 'Cross', 'Race'],
        "rightAnswer": 1
    },
    2: {
        "questions": "Which of these cartoon characters is a rodent?",
        "answers": ['Tasmanian Devil', 'Road Runner', 'Wile E. Coyote', 'Speedy Gonzalez'],
        "rightAnswer": 2
    },
    3: {
        "questions": "What were the first two initials of the character played by Larry Hagman in 'Dallas'?",
        "answers": ['JD', 'JR', 'JG', 'JC'],
        "rightAnswer": 3
    },
    4: {
        "questions": "Which month of the year was named after Julius Caesar?",
        "answers": ['October', 'June', 'July', 'August'],
        "rightAnswer": 2
    },
    5: {
        "questions": "In which Broadway musical did actress Glenn Close star in 1995?",
        "answers": ['Phantom Of The Opera', 'Oklahoma!', 'Miss Saigon', 'Sunset Boulevard'],
        "rightAnswer": 1
    },
    6: {
        "questions": "Which of these celebrities was not a member of the 'Rat Pack'?",
        "answers": ['Joey Bishop', 'Frank Sinatra', 'Sammy Davis Jr.', 'Rock Hudson'],
        "rightAnswer": 0
    },
    7: {
        "questions": "In what city does the singer meet 'Mr. Bojangles'?",
        "answers": ['New Orleans', 'Tallahassee', 'New York', 'Charlotte'],
        "rightAnswer": 0
    },
    8: {
        "questions": "How many X's are there on a regular clock face with Roman numerals?",
        "answers": ['2', '4', '5', '3'],
        "rightAnswer": 1
    }
}


def printPayout(indexCurrent):
    for index, data in enumerate(payouts):
        print(f"  {'->' if index == indexCurrent-1 else '  '} {data}")


def printAnswer(questionIndex, questionList):
    for i in questionList:
        print(f'{chr(65+i)}. {questions[chosen[questionIndex]]["answers"][i]}')


def get5050(question):
    x = [question["rightAnswer"]]
    y = random.choice([0, 1, 2, 3])
    while y == x[0]:
        y = random.choice([0, 1, 2, 3])
    x.append(y)
    return x


def askAudience(question):
    y = []
    for x in range(len(question["answers"])):
        y += list(str(x)*random.randint(1, 100 if x ==
                                        question["rightAnswer"] else 35))
    for x in range(len(question["answers"])):
        question["answers"][x] += f"  {(y.count(str(x))/len(y))*100:.2f}%"


chosen = [x for x in range(len(questions))]
random.shuffle(chosen)
chosen = chosen[:5]
currentPayout = 5
currentQuestion = 0

while currentQuestion < len(chosen):
    answers = [x for x in range(
        len(questions[chosen[currentQuestion]]["answers"]))]
    printPayout(currentPayout)
    print(questions[chosen[currentQuestion]]["questions"])
    userHint = input("Need help(Y/N)? ").upper()
    if len(userHint) != 1:
        continue
    elif userHint == "Y":
        userHintInput = input("A. 50:50\t\tB. Ask audience\n> ").upper()
        if len(userHintInput) != 1:
            continue
        elif userHintInput == "A":
            answers = get5050(questions[chosen[currentQuestion]])
        elif userHintInput == "B":
            askAudience(questions[chosen[currentQuestion]])
        else:
            pass
    printAnswer(currentQuestion, answers)
    userAnswer = input("Your answer (A/B/C/D)? ").upper()
    ordAnswer = ord(userAnswer)-65
    if len(userAnswer) != 1:
        continue
    elif ordAnswer > 3:
        continue
    if questions[chosen[currentQuestion]]["rightAnswer"] == ordAnswer:
        currentPayout -= 1
        currentQuestion += 1
    else:
        break

print(f"You win ${payouts[currentPayout]}")
