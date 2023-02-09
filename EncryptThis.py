#   https://www.codewars.com/kata/5848565e273af816fb000449
#   You want to create secret messages which can be deciphered by the Decipher this! kata. 
#   Here are the conditions:
#   1. Your message is a string containing space separated words.
#   2. You need to encrypt each word in the message using the following rules:
#       - The first letter must be converted to its ASCII code.
#       - The second letter must be switched with the last letter
#   Keepin' it simple: There are no special characters in the input.

def encrypt_this(text):
    text_to_list = text.split(" ")
    list = []
    for word in text_to_list:
        if len(word) == 1:
            first_letter = str(ord(word[0]))
            list.append(first_letter)
        elif len(word) == 2:
            first_letter = str(ord(word[0]))
            two_char = f"{first_letter}{word[-1]}"
            list.append(two_char)
        elif len(word) > 1:
            first_letter = str(ord(word[0]))
            replacement = word[1]
            full_text = f"{first_letter}{word[-1]}{word[2:-1]}{replacement}"
            list.append(full_text)
    return " ".join(list)
