import re
import pprint


def search(sequences, ord_minc, curr_word, current_path, current_path_len, longest_path):
    # Set the current_path based on the current_path_len and incrementing it
    current_path[current_path_len] = curr_word
    current_path_len += 1

    # Checks if current_path_len is bigger than longest_path
    # if so, make a copy of longest_path and then assign
    # the current_path (until current_path_len) to the longest_path
    if current_path_len > len(longest_path):
        longest_path[:] = current_path[:current_path_len]

    # Getting the index (for sequence list) of the last character in curr_word
    last_char_index = ord(curr_word[-1]) - ord_minc
    # Checking if the index is in range of the list
    if last_char_index >= 0 and last_char_index < len(sequences):
        for pair in sequences[last_char_index]:
            if not pair[1]:
                pair[1] = True
                search(sequences, ord_minc,
                       pair[0], current_path, current_path_len, longest_path)
                pair[1] = False


def findLongestSeries(filename):
    with open(filename, "r") as handler:
        names = re.findall("[a-z]+", handler.read())

    # Getting the minimum ascii value from the lists
    ord_minc = ord(min(name[0] for name in names))
    # Getting the maximum ascii value from the lists
    ord_maxc = ord(max(name[0] for name in names))

    # Initializing the array that will be used for
    # categorizing the pokemons
    sequences = [[] for _ in range(ord_maxc - ord_minc + 1)]
    # Categorizing all of the pokemons into their respective
    # characters (ascii value)
    for name in names:
        # Appending the `[pokemonsName, isUsed]` into the list
        sequences[ord(name[0]) - ord_minc].append([name, False])
    current_path = [None] * len(names)
    longest_path = []

    for seq in sequences:
        for pair in seq:
            pair[1] = True
            search(sequences, ord_minc, pair[0], current_path, 0, longest_path)
            pair[1] = False

    return longest_path


print(findLongestSeries("pokemons.txt"))
