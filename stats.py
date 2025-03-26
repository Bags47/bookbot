# This function counts the number of words
def count_words(book_text):
    return len(book_text.split())

# This function counts the number of characters
def count_characters(book_text):
    book_text = book_text.lower()
    char_count = {}
    for char in book_text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# This function returns sorted dictionaries of characters and their counts
def sort_character_count(char_count_dict):
    sorted_list = [
        {"char": char, "count": count}
        for char, count in char_count_dict.items()
    ]
    sorted_list.sort(key=lambda c: c["count"], reverse=True)
    return sorted_list