#   https://www.codewars.com/kata/526571aae218b8ee490006f4
#   Write a function that takes an integer as input, and returns the number of bits 
#   that are equal to one in the binary representation of that number. 

def count_bits(n):
    binary_representation = (bin(n)[2:])
    return binary_representation.count("1")

def main():
    number = 11
    print(f"Number of bits that are equal to 1 in the binary representation of {number} is {count_bits(number)}.")

if __name__ == "__main__":
    main()
