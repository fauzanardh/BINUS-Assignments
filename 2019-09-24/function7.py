# roman to arabic and vice versa

def romanArabic(arg):
    if type(arg) == int:
        result = ""
        i = 0
        conv = [[10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
        while arg > 0:
            while conv[i][0] > arg: i+=1
            result += conv[i][1]
            arg -= conv[i][0]
        print(result)
    elif type(arg) == str:
        arg = arg.upper()
        count = 0
        while "IV" in arg:
            count += 4
            arg = arg.replace("IV", "", 1)
        while "IX" in arg:
            count += 9
            arg = arg.replace("IX", "", 1)
        while "I" in arg:
            count += 1
            arg = arg.replace("I", "", 1)
        while "V" in arg:
            count += 5
            arg = arg.replace("V", "", 1)
        while "X" in arg:
            count += 10
            arg = arg.replace("X", "", 1)
        print(count)
    else:
        print("Type not supported")

romanArabic("XIX")
romanArabic(19)