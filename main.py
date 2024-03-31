def sort_key(dict):
    return dict["num"]


def letter_dict_to_list(dict):
    letter_list = []
    for letter in dict:
        letter_list.append({"letter": letter, "num": dict[letter]})
    letter_list.sort(reverse=True, key=sort_key)
    return letter_list


def word_count_of(str):
    return len(str.split())


def letter_counts(str):
    letter_dict = {}
    for i in range(0, len(str)):
        letter = str[i].lower()
        if (letter.isalpha()):
            if (letter in letter_dict):
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        letter_list = letter_dict_to_list(letter_counts(file_contents))
        print("...begin report of books/frankenstein.txt...")
        print(f"There are {word_count_of(file_contents)} words in this book \n")
        for i in range(0, len(letter_list)):
            print(f"There are {letter_list[i]['num']} {letter_list[i]['letter']}'s")
        print("...end report...")


main()
