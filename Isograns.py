#   https://www.codewars.com/kata/54ba84be607a92aa900000f1
#   An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
#   Implement a function that determines whether a string that contains only letters is an isogram. 
#   Assume the empty string is an isogram. Ignore letter case.

#   isIsogram "Dermatoglyphics" = true
#   isIsogram "moose" = false
#   isIsogram "aba" = false

def is_isogram(string):
    string_lower = string.lower()
    return all(not x for x in string if string_lower.count(x) > 1)
