def appendLine(inputFile, outputFile):
    _temp = ""
    _acc = 1
    for line in open(inputFile):
        _temp += f"{_acc} | {line}"
        _acc += 1
    with open(outputFile, "w+") as handler:
        handler.write(_temp)


appendLine("e2_input.txt", "e2_output.txt")
