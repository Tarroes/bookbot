def num_words(text):
    words = text.split()
    print(f"{len(words)} words found in the document")
    print("--------- Character Count -------")

def sort_on(items):
    return items["num"]

def char_frequency(text):
    frequency = {}
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            char = char.lower()  # Normalize to lowercase
            frequency[char] = frequency.get(char, 0) + 1
    return frequency