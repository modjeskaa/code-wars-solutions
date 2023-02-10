#   https://www.codewars.com/kata/5412509bd436bd33920011bc
#   Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(word):
    if len(word) <= 4:
        return word
    elif word == None:
        return " "
    else:
        last_four = word[-4:]
        hash = "#" * len(word[:-4])
        return f"{hash}{last_four}"
