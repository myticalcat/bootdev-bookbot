from stats import get_num_words, get_characters_count
import sys

def get_book_text(file_path : str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    path_to_book = sys.argv[1]
    print(f"""============ BOOKBOT ============
Analyzing book found at {path_to_book}...""")
    book = get_book_text(path_to_book)
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")
    sorted_char = sorted(tuple(get_characters_count(book).items()), key=lambda x : x[1], reverse=True)
    for t in sorted_char:
        if t[0].isalpha():
            print(f"{t[0]}: {t[1]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()