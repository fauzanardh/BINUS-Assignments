import re


nsolutions = 0


def search(sequences, ord_minc, curr_word, current_path, current_path_len, longest_path):
    global nsolutions

    current_path[current_path_len] = curr_word
    current_path_len += 1

    if current_path_len == len(longest_path):
        nsolutions += 1
    elif current_path_len > len(longest_path):
        nsolutions = 1
        longest_path[:] = current_path[:current_path_len]

    last_char_index = ord(curr_word[-1]) - ord_minc
    if last_char_index >= 0 and last_char_index < len(sequences):
        for pair in sequences[last_char_index]:
            if not pair[1]:
                pair[1] = True
                search(sequences, ord_minc, pair[0], current_path,
                       current_path_len, longest_path)
                pair[1] = False


def findLongestSeries(filename):
    with open(filename, "r") as handler:
        names = re.findall("[a-z]+", handler.read())

    ord_minc = ord(min(name[0] for name in names))
    ord_maxc = ord(max(name[0] for name in names))
    sequences = [[] for _ in range(ord_maxc - ord_minc + 1)]
    for name in names:
        sequences[ord(name[0]) - ord_minc].append([name, False])

    current_path = [None] * len(names)
    longest_path = []

    for seq in sequences:
        for pair in seq:
            pair[1] = True
            search(sequences, ord_minc, pair[0],
                   current_path, 0, longest_path)
            pair[1] = False

    return longest_path


print(findLongestSeries("pokemons.txt"))
