# Q6c) Find the maximum nested depth of curly braces
#
# Unbalanced or wrongly ordered braces should return -1
#
# Iterating over input string is one way to solve this, another is to use regular expressions
import re


def max_nested_braces(string_):
    braces = []
    nesting = 0

    # eliminate empty braces
    if re.search(r'{}', string_):
        return -1

    for char in string_:
        if char == '{' or char == '}':
            braces.append(char)

    # unbalanced eliminated
    if len(braces) % 2 != 0:
        return -1

    # wrongly ordered eliminated
    half = braces[:int(len(braces)/2)]
    if half.count('}') > half.count('{'):
        return -1

    # try to follow this logic
    total_ride = len(braces) / 2  # the total distance of the list 'braces' we shall travel
    ball_gum = 0

    while total_ride > 0:
        char = braces[ball_gum]
        ball_gum += 1

        if char == '{':
            # if it's an opening curly brace increment nesting depth
            nesting += 1
            # total ride decremented only when it's a '{'
            total_ride -= 1

        elif char == '}':
            # if it closes decrement depth by 1 and leave total ride the same!
            nesting -= 1

    return nesting


print(max_nested_braces('a*b'))
# 0
print(max_nested_braces('{a+2}*{b+c}'))
# 1
print(max_nested_braces('{{a+2}*{{b+{c*d}}+e*d}}'))
# 4
print(max_nested_braces('a*b+{}'))
# 1
print(max_nested_braces('}a+b{'))
# -1
print(max_nested_braces('a*b{'))
# -1

# bonus: empty braces, i.e {} should return -1
print(max_nested_braces('a*b+{}'))
# -1
print(max_nested_braces('a*{b+{}+c*{e*3.14}}'))
# -1
