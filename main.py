#import word counter from stats.py
from stats import num_words
from stats import char_frequency
from stats import sort_on


import sys

if len(sys.argv) == 2:
    book_path = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

#Read book from path and convert to string
def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents


# Main function to read a book and count the number of words
# in the book using the num_words function from stats.py
# This function is called when the script is run directly.
# It takes the path to the book as an argument.

def main(book_path):
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path)
    print("----------- Word Count ----------")
    book_text = get_book_text(book_path)
    num_words(book_text)
    char_freq = char_frequency(book_text)
    new_dict = {}
    new_list =[]
    for key, value in char_freq.items():
        new_dict = {"char": key, "num": value}
        new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    
    for dictionary in new_list:
        char = dictionary["char"]
        num = dictionary["num"]
        if char.isalpha():
            print(char + ": " + str(num))
    print("============= END ===============")

main(book_path)