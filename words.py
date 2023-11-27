def print_upper_words(words, must_start_with):
    '''Prints out each word in a list in uppercase
    if the word starts with one of the submitted letters'''
    for word in words:
        if type(word) == str:
            for letter in must_start_with:
                if type(letter) == str and word[0] == letter:
                    print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})