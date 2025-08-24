import sys
from stats import number_of_words
from stats import number_of_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents
    
def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    number_of_words(book_text)
    print("--------- Character Count -------")
    number_of_chars(book_text)
    print("============= END ===============")

if __name__ == "__main__":
    main() 