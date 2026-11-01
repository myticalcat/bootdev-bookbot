from stats import get_num_words

def get_book_text(file_path : str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    print(f"Found {get_num_words(book)} total words")


if __name__ == "__main__":
    main()