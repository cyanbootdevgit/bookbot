from stats import get_num_words, count_symbols, sort_dictionary
import sys

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    # do something with f (the file) here
    return file_contents

def print_nicely(s_list, wordcount, filename):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}")
    print(f"----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print(f"--------- Character Count -------")

    for symbol in s_list:
        if symbol["letter"].isalpha():
            print(f"{symbol["letter"]}: {symbol["num"]}")
    
    print(f"============= END ===============")
    

def main():
    #filename = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filename = sys.argv[1]
    book_string = get_book_text(filename)
    
    print_nicely(sort_dictionary(count_symbols(book_string)), get_num_words(book_string), filename)

main()