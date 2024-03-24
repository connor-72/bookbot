import string

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path)
    count = word_count(book_contents)
    char_dict = char_count(book_contents)
    sorted_dict = sort_dict(char_dict)
    print("--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    for k,v in sorted_dict.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

def sort_dict(dictionary):
    sorted_lst = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    result = dict(sorted_lst)
    return result

def char_count(text):
    lowered = text.lower()
    letters = dict.fromkeys(string.ascii_lowercase, 0)
    for letter in letters:
        letters[letter] = lowered.count(letter)
    return letters

def word_count(text):
    words = text.split()
    return len(words)

def get_book_contents(path):
    with open(path) as f:
        return f.read()

main()