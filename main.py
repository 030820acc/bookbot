def letter_dict_to_list(dict):
    letter_list = []
    for letter in dict:
        letter_list.append({"letter": letter, "num": dict[letter]})
    return letter_list


def word_count_of(str):
    return len(str.split())


def letter_counts(str):
    letter_dict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    for i in range(0, len(str)):
        letter = str[i].lower()
        if (letter in letter_dict):
            letter_dict[letter] += 1
    return letter_dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        letter_list = letter_dict_to_list(letter_counts(file_contents))
        print(word_count_of(file_contents))
        for i in range(0, len(letter_list)):
            print(f"There are {letter_list[i]['num']} {letter_list[i]['letter']}'s")


main()
