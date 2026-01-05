import sys
from stats import (
    get_number_of_words,
    get_occurences_of_letters,
    get_sorted_dict_list,
    print_character_report,
    print_word_report,
)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text_as_string = f.read()
    return book_text_as_string


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text_as_string = get_book_text(book_path)
    number_of_words = get_number_of_words(book_text_as_string)
    occurences_of_letters = get_occurences_of_letters(book_text_as_string)
    print_word_report(book_path)
    print(f"Found {number_of_words} total words")
    sorted_dict_list = get_sorted_dict_list(occurences_of_letters)
    print_character_report(sorted_dict_list)


main()
