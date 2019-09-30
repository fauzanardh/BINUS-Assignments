studentsList = [
    {
        "name": "Eren",
        "homework": [90.0, 97.0, 75.0, 92.0],
        "quizzes": [88.0, 40.0, 94.0],
        "tests": [75.0, 90.0]
    },
    {
        "name": "Mikasa",
        "homework": [100.0, 92.0, 98.0, 100.0],
        "quizzes": [82.0, 83.0, 91.0],
        "tests": [89.0, 97.0]
    },
    {
        "name": "Armin",
        "homework": [0.0, 87.0, 75.0, 22.0],
        "quizzes": [0.0, 75.0, 78.0],
        "tests": [100.0, 100.0]
    }
]


def average(nums):
    return sum(nums)/len(nums)


def getAverage(student):
    return average(student["homework"])*0.1 + average(student["quizzes"])*0.3 + average(student["tests"])*0.6


def getClassAverage(students):
    return sum([getAverage(student) for student in students])/len(students)


def getLetterGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


for student in studentsList:
    printout = f"{student['name']}\n"
    printout += f"{student['homework']}\n"
    printout += f"{student['quizzes']}\n"
    printout += f"{student['tests']}\n"
    score = getAverage(student)
    printout += f"average: {score:.2f} -> {getLetterGrade(score)}"
    print(printout)

classscore = getClassAverage(studentsList)
print(f"class average: {classscore:.2f} -> {getLetterGrade(classscore)}")
