from stats import count_words, count_characters, sort_character_count
import sys



# This function reads the file
def get_book_text(filepath):
    try:
        with open(filepath, 'r') as book_file:
            return book_file.read()
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        sys.exit(1)

# This functions prints the contents
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    # Gets word count
    word_count = count_words(book_text)

    #Gets character count
    char_count = count_characters(book_text)

    #Gets sorted characters
    sorted_chars = sort_character_count(char_count)
   
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")

    print("============= END ===============")

# Excutes the program
if __name__ == '__main__':
    main()
