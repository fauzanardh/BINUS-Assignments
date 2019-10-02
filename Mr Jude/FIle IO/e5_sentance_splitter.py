import re


def sentanceSplitter(filename):
    with open(filename, "r") as handler:
        data = handler.read()
    sentences = re.sub(r"(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])", r".\n\1", data)
    sentences = re.sub(r"!\s", "!\n", sentences)
    sentences = re.sub(r"\?\s", "?\n", sentences)
    return sentences


print(sentanceSplitter("sentence.txt"))
