import sys

from stats import get_num_words
from stats import get_character_counts
from stats import convert_to_sorted_list


def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book = sys.argv[1]

    book_text = get_book_text(book)

    word_count = get_num_words(book_text)

    character_counts = get_character_counts(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in convert_to_sorted_list(character_counts):
        if dict["character"].isalpha():
            print(f'{dict["character"]}: {dict["count"]}')
    print("============= END ===============")

if __name__=="__main__":
    main()
