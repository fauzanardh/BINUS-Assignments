import json

with open("colors.json", "r") as fp:
    colors = json.loads(fp.read())


def saveFile(outfile, jsonData):
    with open(outfile, "w") as fp:
        fp.write(json.dumps(jsonData, indent=4))


def hexToIndex(hexString):
    for index, color in enumerate(colors["colors"]):
        if color["code"]["hex"] == hexString.upper():
            return index
    return -1


def colorToIndex(colorInput):
    recommend = []
    for index, color in enumerate(colors["colors"]):
        if color["color"] == colorInput.lower():
            return index
        elif colorInput.lower() in color["color"]:
            recommend.append(index)
    if recommend == []:
        return -1
    return recommend


def rgbToIndex(rgbString):
    rgbVal = rgbString.replace(" ", "").split(",")
    rgbVal = [int(rgb) for rgb in rgbVal]
    for index, color in enumerate(colors["colors"]):
        if color["code"]["rgb"] == rgbVal:
            return index
    return -1


def addColor():
    color = input("Color (ex. white): ").lower()
    rgbVal = input("RGB String (ex. 255,255,255): ").replace(
        " ", "").split(",")
    hexString = input("HexString (ex. FFFFFF): ").upper()
    colors["colors"].append({
        "color": color,
        "code": {
            "rgb": rgbVal,
            "hex": hexString
        }
    })
    saveFile("colors.json", colors)


availableChoice = ['1', '2', '3', '4']
while True:
    print("1. Find by Color\n2. Find by RGB\n3. Find by HexString\n4. Add color")
    choice = input("> ")
    colorFoundIndex = -1
    isSave = False
    if choice not in availableChoice:
        continue
    if choice == '1':
        colorFoundIndex = colorToIndex(input("Color (ex. white): "))
    elif choice == '2':
        colorFoundIndex = rgbToIndex(
            input("RGB String (ex. 255,255,255): "))
    elif choice == '3':
        colorFoundIndex = hexToIndex(input("HexString (ex. FFFFFF): "))
    elif choice == '4':
        isSave = True
        addColor()
    else:
        continue
    if isSave:
        pass
    elif colorFoundIndex == -1:
        print("Color not found")
    elif type(colorFoundIndex) is list:
        print("Color not found")
        for x in colorFoundIndex:
            print(f'Recommended: {str(colors["colors"][x])}')
    else:
        print(colors["colors"][colorFoundIndex])
