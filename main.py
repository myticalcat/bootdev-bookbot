from stats import get_num_words, get_characters_count

def get_book_text(file_path : str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    print(f"Found {get_num_words(book)} total words")
    print(f"{get_characters_count(book)}")

if __name__ == "__main__":
    main()