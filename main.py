import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

from stats import num_words, num_of_characters,convert

def main():
    content = get_book_text(sys.argv[1])
    number = num_words(content)
    char = num_of_characters(content)
    sort = convert(char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for x in sort:
        if x["char"].isalpha():
            print(x["char"] + ":" + " " + str(x["num"]))
    print("============= END ===============")

main()