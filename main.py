from stats import get_num_words, get_characters_count

def get_book_text(file_path : str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    print(f"Found {get_num_words(book)} total words")
    sorted_char = sorted(tuple(get_characters_count(book).items()), key=lambda x : x[1], reverse=True)
    print(f"{sorted_char}")

if __name__ == "__main__":
    main()