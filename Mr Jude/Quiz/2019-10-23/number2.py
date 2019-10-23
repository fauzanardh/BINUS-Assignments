import re


class Staff:
    def __init__(self, _id, name, position, salary):
        self.__id = _id
        self.name = name
        self.__position = position
        self.__salary = salary

    def __str__(self):
        return f"Staff(_id={self.__id}, name={self.name}, position={self.__position}, salary={self.__salary})"

    def __repr__(self):
        return f"Staff(_id={self.__id}, name={self.name}, position={self.__position}, salary={self.__salary})"

    def __eq__(self, strID):
        return self.__id == strID

    def getID(self):
        return self.__id

    def getPosition(self):
        return self.__position

    def getSalary(self):
        return self.__salary


positions = {
    "STAFF": {
        "min": 3500000,
        "max": 7000000
    },
    "OFFICER": {
        "min": 7000001,
        "max": 10000000
    },
    "MANAGER": {
        "min": 10000001,
        "max": 1E+128
    }
}


def loadData(filename):
    staffs = []
    for line in open(filename, 'r'):
        spl = line.rstrip().split('#')
        staffs.append(Staff(spl[0], spl[1], spl[2], spl[3]))
    return staffs


def saveData(staffs, filename):
    # making a temp variable to hold the staffs
    # so you don't have use fp.write multiple times
    # it is more efficient
    _temp = ""
    for staff in staffs:
        _temp += f"{staff.getID()}#{staff.name}#{staff.getPosition()}#{staff.getSalary()}\n"
    with open(filename, 'w') as fp:
        fp.write(_temp)


def printStaffs(staffs):
    data = [["ID", "Name", "Position", "Salary Amount"]]
    data += [[staff.getID(), staff.name, staff.getPosition(), staff.getSalary()]
             for staff in staffs]
    col_width = max(len(word) for row in data for word in row) + 2
    for row in data:
        print("|".join(word.ljust(col_width) for word in row))


def mainMenu(staffs):
    printStaffs(staffs)
    while True:
        print("\n1. New Staff\n2. Delete Staff\n3. View Summary Data\n4. Save & Exit")
        try:
            choice = int(input("Your Choice: "))
            if choice == 1:
                while True:
                    _id = input("Input desired id [SXXXX]: ")
                    if not re.match(r"S\d{4}", _id):
                        print("The format have to be SXXXX!")
                        continue
                    name = input("Input name [0..20]: ")
                    if len(name) >= 20:
                        print("Your name must not exceed 20 characters!")
                        continue
                    position = input(
                        "Input desired position [staff|officer|manager]: ").upper()
                    if position not in positions:
                        print("Position not available!")
                        continue
                    try:
                        salary = int(input(
                            f"Input desired salary for {position} [{positions[position]['min']}..{positions[position]['max']}]: "))
                        if not (salary >= positions[position]["min"] and salary <= positions[position]["max"]):
                            print("Salary not in range!")
                            continue
                    except ValueError:
                        print("Salary have to be int!")
                        continue
                    staff = Staff(_id, name, position, salary)
                    staffs.append(staff)
                    print(f"Successfully added a new staff!\n{staff}")
                    break
            elif choice == 2:
                idDelete = input("Input id [SXXXX]")
                if not re.match(r"S\d{4}", idDelete):
                    print("The format have to be SXXXX!")
                    continue
                if idDelete not in staffs:
                    print("ID not found!")
                    continue
                staffs.pop(staffs.index(idDelete))
                print("ID Removed!")
            elif choice == 3:
                staffSal = []
                officerSal = []
                managerSal = []
                for staff in staffs:
                    if staff.getPosition() == "STAFF":
                        staffSal.append(int(staff.getSalary()))
                    elif staff.getPosition() == "OFFICER":
                        officerSal.append(int(staff.getSalary()))
                    elif staff.getPosition() == "MANAGER":
                        managerSal.append(int(staff.getSalary()))
                printOut = "1. Staff\n"
                printOut += f"Minimum Salary: {positions['STAFF']['min']}\n"
                printOut += f"Maximum Salary: {positions['STAFF']['max']}\n"
                try:
                    printOut += f"Average Salary: {sum(staffSal)/len(staffSal)}\n\n"
                except ZeroDivisionError:
                    printOut += "Average Salary: 0\n\n"
                printOut += "2. Officer\n"
                printOut += f"Minimum Salary: {positions['OFFICER']['min']}\n"
                printOut += f"Maximum Salary: {positions['OFFICER']['max']}\n"
                try:
                    printOut += f"Average Salary: {sum(officerSal)/len(officerSal)}\n\n"
                except ZeroDivisionError:
                    printOut += "Average Salary: 0\n\n"
                printOut += "3. Manager\n"
                printOut += f"Minimum Salary: {positions['MANAGER']['min']}\n"
                printOut += f"Maximum Salary: {positions['MANAGER']['max']}\n"
                try:
                    printOut += f"Average Salary: {sum(managerSal)/len(managerSal)}\n\n"
                except ZeroDivisionError:
                    printOut += "Average Salary: 0\n\n"
                print(printOut)
            elif choice == 4:
                break
        except ValueError:
            continue


stfs = loadData('number2_data.txt')
mainMenu(stfs)
saveData(stfs, 'number2_data.txt')
