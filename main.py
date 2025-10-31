from stats import get_book_words, get_book_char, sort_char
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")

    book_path = sys.argv[1]

    def get_book_text(path):
        with open(path) as f:
            return f.read()
    
    text = get_book_text(book_path)
    word_count = get_book_words(text)
    book_stats = get_book_char(text)
    report = sort_char(book_stats)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    sorted_report = sort_char(book_stats)
    for item in sorted_report:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    
main()
