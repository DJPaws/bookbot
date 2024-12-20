def main():
    char_count = {} # Dictionary for letter count

    book_path = "/root/workspace/github.com/DJPaws/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document") # Prints total word count within the document
    print() # Prints blank space
    
    # Counts each letter and give it a value based on how many times its used
    for character in text:
        lowercase_character = character.lower()
        if lowercase_character.isalpha():
            if lowercase_character in char_count:
                char_count[lowercase_character] += 1
            else:
                char_count[lowercase_character] = 1
    
    # Sorts each letter alphabetically then print results to terminal
    sorted_characters = sorted(char_count.keys())
    for character in sorted_characters:
        print(f"The '{character}' character was found {char_count[character]} times")

# Total word count in document
def get_num_words(text):
    words = text.split()
    return len(words)

# Open and return the document contents
def get_book_text(path):
    with open(path) as f:
        return f.read()

# execute code with a header and footer
if __name__ == "__main__":
    print("--- Report Start ---") # Header
    main()
    print("--- Report End ---") # Footer
