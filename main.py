from stats import get_num_words, get_chars_count, dictionaries_list
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    get_num_words(get_book_text(sys.argv[1]))
    #print(dictionaries_list(get_chars_count(get_book_text("./books/frankenstein.txt"))))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")

    sorted_dictionaries_list = dictionaries_list(get_chars_count(get_book_text(sys.argv[1])))
    for item in sorted_dictionaries_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()