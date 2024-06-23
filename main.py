def count_words(content):
    words = content.split()
    print(len(words))

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    count_words(file_contents)



main()