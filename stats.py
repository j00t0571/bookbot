def get_num_words(book_text):
    book_words = book_text.split()
    return len(book_words)
    #book_words_count = len(book_words)
    #print(f"{book_words_count} words found in the document")

def get_chars_count(book_text):
    chars_count = {char: num for char, num in []}
    
    for char in book_text:
        char = char.lower()
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1

    return chars_count

def sort_on(dict):
    return dict["num"]

def dictionaries_list(chars_count):
    sorted_dictionaries_list = []

    for key, value in chars_count.items():
        sorted_dictionaries_list.append({"char": key, "num": value})
                                        
    sorted_dictionaries_list.sort(reverse=True, key=sort_on)
    return sorted_dictionaries_list