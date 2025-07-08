#import word counter from stats.py
from stats import num_words
from stats import char_frequency


book_path = "books/frankenstein.txt"


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
    book_text = get_book_text(book_path)
    num_words(book_text)
    char_freq = char_frequency(book_text)
    print(char_freq)

main(book_path)