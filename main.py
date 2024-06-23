def count_words(content):
    words = content.split()
    return len(words)

def count_chars(content):
    content = content.lower()
    chars = {}
    for word in content:
        if word in chars:
            chars[word] += 1
        else:
            chars[word] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def char_sorted(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key= sort_on)
    return sorted_list

def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    
    number_of_words = count_words(file_contents)
    char_dict = count_chars(file_contents)
    char_dict = char_sorted(char_dict)

    print(f"--- Begin report of {book} ---")
    print(f"{number_of_words} words found in the document")
    print()
    for char in char_dict:
        if not char["char"].isalpha():
            continue
        print(f"The {char['char']} character was found {char['num']} times")
    
    print("--- End report ---")


main()