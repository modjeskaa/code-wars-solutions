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

print(encrypt_this("A wise old owl lived in an oak"))
