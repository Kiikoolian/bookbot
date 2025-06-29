

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


    sorted_letters = dict(sorted(num_letters.items(), key=lambda item: item[1], reverse=True))
    return sorted_letters

