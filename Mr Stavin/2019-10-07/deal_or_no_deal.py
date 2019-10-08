import random

# state enum
# 0 = discarded
# 1 = not discarded
# 2 = chosen


def initiateBriefcases():
    briefcasePayout = [
        "1",
        "5",
        "10",
        "25",
        "50",
        "75",
        "100",
        "200",
        "300",
        "400",
        "500",
        "750",
        "1000",
        "5000",
        "10000",
        "25000",
        "50000",
        "75000",
        "100000",
        "200000",
        "300000",
        "400000",
        "500000",
        "750000",
        "1000000"
    ]
    random.shuffle(briefcasePayout)
    briefcases = {}
    for index, data in enumerate(briefcasePayout):
        briefcases[str(index+1)] = data
    return briefcases


briefcases = initiateBriefcases()
total = []
while len(briefcases) > 1:
    print(" ".join(briefcases.keys()))
    if (len(total) > 1) and (len(total) % 5 == 0):
        print(f"Banker offers ${sum(total)/len(total)} for your briefcase")
        xInput = input("Do you agree (y/n)? ").lower()
        if xInput == "y":
            break
    bcNum = input("\nBriefcase number? ")
    if bcNum not in briefcases:
        print(f"There's no briefcase with {bcNum} number")
        continue
    print(f"Briefcase {bcNum} with ${briefcases[bcNum]} deleted!")
    total.append(int(briefcases[bcNum]))
    del briefcases[bcNum]

if len(briefcases) == 1:
    print(f"Yay, you got {briefcases}")
else:
    print(f"You accepted the banker's offer of {sum(total)/len(total)}")
