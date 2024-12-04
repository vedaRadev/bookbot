BOOK_PATH = "./books/frankenstein.txt"

# file will be closed at the end of the with block
# would have to do this myself if I did `f = open(BOOK_PATH)`
# this is just RAII
with open(BOOK_PATH) as f:
    book = f.read()

    num_words = len(book.split())

    char_counts = {}
    for c in book.lower():
        if not c.isalpha():
            continue

        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1

    print(f"--- Begin report of {BOOK_PATH} ---")
    print(f"{num_words} words found in the document")
    print()
    for c in char_counts:
        count = char_counts[c]
        print(f"The '{c}' character was found {count} times")
    print("--- End report ---")

