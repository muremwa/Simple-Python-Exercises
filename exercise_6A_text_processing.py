# Q6a) Check if two words are same or differ by only one character (irrespective of case),
# input strings should have same length


def is_one_char_diff(string_1, string_2):
    # lengths do not match
    if len(string_1) != len(string_2):
        return False

    string_1 = string_1.upper()
    string_2 = string_2.upper()

    # the real work begins
    counter = 0     # increment if don't match
    for k, char in enumerate(string_1):
        if string_2[k] != char:
            counter += 1

    if counter > 1:
        return False
    else:
        return True


print(is_one_char_diff('bar', 'bar'))
# True
print(is_one_char_diff('bar', 'Baz'))
# True
print(is_one_char_diff('Food', 'fold'))
# True
print(is_one_char_diff('A', 'b'))
# True
#

print('\n')

print(is_one_char_diff('a', ''))
# False
print(is_one_char_diff('Bar', 'Bark'))
# False
print(is_one_char_diff('Bar', 'art'))
# False
print(is_one_char_diff('Food', 'fled'))
# False
print(is_one_char_diff('ab', ''))
# False
