def appendLine(inputFile, outputFile):
    with open(outputFile, "w+") as handler:
        for index, line in enumerate(open(inputFile, "r")):
            handler.write(f"{index+1} | {line}")


appendLine("e2_input.txt", "e2_output.txt")
