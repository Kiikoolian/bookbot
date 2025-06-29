

def get_num_words(book):
   
    book_split = book.split()
    num_words = len(book_split)
    return f"{num_words} total words"

def get_num_letters(book):
      
    book_split = book.split()
    letters = []    
    num_letters = {}

    for word in book_split:
        for letter in word:
            if letter.isalpha():
                letters.append(letter.lower())  # Collect letters directly, lowercase optional

    for ltr in letters:
        if (ltr in num_letters):
            num_letters[ltr] += 1
        else:
            num_letters[ltr] = 1

    #.items returns a liste of tuples (double entry tabs ex: ( [5][33] , [54][45] ) )
    # key=lambda item: item[1] , Each item is a tuple like ('e', 5), item[0] is the key ('e') and item[1] is the value (5)
    # So lambda item: item[1] tells Python: "When you're sorting, use the value part of each (key, value) pair." here Lambda can me we dont care about key , we want the value to be treated
    sorted_letters = dict(sorted(num_letters.items(), key=lambda item: item[1], reverse=True))
    return sorted_letters

