#   https://www.codewars.com/kata/520b9d2ad5c005041100000f
#   Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
#   Leave punctuation marks untouched.

#   Examples:
#   pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#   pig_it('Hello world !')     # elloHay orldway !

import string
def pig_it(text):
    text_to_list = text.split(" ")
    list = []
    punctuation = string.punctuation
    for word in text_to_list:
        if word in punctuation:
            list.append(word)
        elif len(word) == 1:
            list.append(word + "ay")
        elif len(word) >= 2:
            first_letter = str(word[0])
            full_text = f"{word[1:]}{first_letter}ay"
            list.append(full_text)
    return " ".join(list)
