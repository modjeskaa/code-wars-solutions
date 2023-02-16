#   https://www.codewars.com/kata/5410c0e6a0e736cf5b000e69/python
#   The Hamming Distance is a measure of similarity between two strings of equal length. 
#   Complete the function so that it returns the number of positions where the input strings do not match.

def hamming(a,b):
    a_sep_list = [x for x in a]
    b_sep_list = [x for x in b]
    print(a_sep_list)
    print(b_sep_list)
    counter = 0
    count = 0
    while counter != len(a_sep_list):
        for x in a_sep_list:
            if a_sep_list[counter] != b_sep_list[counter]:
                count += 1
            else:
                pass
            counter += 1
        return count
print(hamming("hello world","hello tokyo"))
