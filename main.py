def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    words = count_words(book_text)
    chars = count_characters(book_text)
    print("Begin report!")
    print(f"{words} words found in the document\n\n")
    for char in chars:
        if not char.isalpha():
            continue
        print(f"The {char} character was found {chars[char]} times")

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
    return book_text

def count_characters(text):
    count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count



main()