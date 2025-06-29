from stats import *
import sys

# /!\All comment are my interpretation don't take them at face value/!\

def get_book_text(file_path):

    with open(file_path) as f:
        return f.read()

    


def print_book_report(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    book = get_book_text(file_path)
    word_count = get_num_words(book)
    letter_counts = get_num_letters(book)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for letter, count in letter_counts.items():
        print(f"{letter}: {count}")
    print("============= END ===============")

#__name__ common Python convention used to control script behavior. if run via python myscript.py, __name__ = "__main__" 
if __name__ == "__main__": 
    #sys.argv take 2 value, its a list ... kinda.
    if len(sys.argv) != 2:
        #here, first value is the script name, here"main.py", second is user input value, here "<path_to_book>" ("book/frankenstein,txt" for example)
        print("Usage: python3 main.py <path_to_book>")
        #code erreur 1 if 2 value len not respected 
        sys.exit(1)

    file_path = sys.argv[1]
    print_book_report(file_path)