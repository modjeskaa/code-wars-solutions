#   https://www.codewars.com/kata/54da5a58ea159efa38000836
#   Given an array of integers, find the one that appears an odd number of times.

def find_it(seq):
    for odd in seq:
        if seq.count(odd) % 2 != 0:
            return odd
