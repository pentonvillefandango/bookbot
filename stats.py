def get_number_of_words(book_text_as_string):
    number_of_words = len(book_text_as_string.split())
    return number_of_words


def get_occurences_of_letters(book_text_as_string):
    char_count = {}
    for char in book_text_as_string.lower():
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1
    return char_count


def get_sorted_dict_list(occurences_of_letters):
    sorted_dict_list = sorted(occurences_of_letters.items(), reverse=True, key=sort_on)
    return sorted_dict_list


def sort_on(occurences_of_letters):
    return occurences_of_letters[1]


def print_word_report(book_path):
    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}
----------- Word Count ----------""")


def print_character_report(sorted_dict_list):
    print(
        """
--------- Character Count -------""".lstrip()
    )
    for dict in sorted_dict_list:
        if dict[0].isalpha():
            print(f"{dict[0]}: {dict[1]}")
    print(
        """
============= END ===============""".lstrip()
    )
