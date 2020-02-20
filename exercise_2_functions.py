import re


# 2a) Returns length of integer numbers
def len_int(integer):
    # len_int('a') should give
    # TypeError: provide only integer input
    if type(integer) is not int:
        raise TypeError('provide only integer input')

    integer = str(integer)

    # handle negative numbers
    if integer[0] == '-':
        integer = integer[1:]

    return len(integer)


# Q2b) Returns True/False - two strings are same irrespective of lowercase/uppercase
def str_cmp(string_1, string_2):
    return str(string_1).upper() == str(string_2).upper()


# Q2c) Returns True/False - two strings are anagrams (assume input consists of alphabets only)
def str_anagram(alpha_1, alpha_2):
    return set(str(alpha_1).upper()) == set(str(alpha_2).upper())


# Q2d) Returns corresponding integer or floating-point number
def num(i):
    # num(['1', '2.3']) TypeError: not a valid input
    if type(i) not in [int, float, str]:
        raise TypeError('not a valid input')

    if type(i) == str:
        if re.search(r'[^0-9.]', str(i)):
            raise ValueError('could not convert string to int or float')

        if re.search(r'\d*\.\d', str(i)):
            i = float(i)
        else:
            i = int(i)
    return i
