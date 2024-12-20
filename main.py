def main():
    char_count = {}

    book_path = "/root/workspace/github.com/DJPaws/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print()
    
    for character in text:
        lowercase_character = character.lower()
        if lowercase_character.isalpha():
            if lowercase_character in char_count:
                char_count[lowercase_character] += 1
            else:
                char_count[lowercase_character] = 1
    
    for character in sorted(char_count.keys()):
        print(f"The '{character}' character was found {char_count[character]} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    print("--- Report Start ---")
    main()
    print("--- Report End ---")