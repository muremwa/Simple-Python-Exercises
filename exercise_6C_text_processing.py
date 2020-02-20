# Q6c) Find the maximum nested depth of curly braces
#
# Unbalanced or wrongly ordered braces should return -1
#
# Iterating over input string is one way to solve this, another is to use regular expressions
import re


def max_nested_braces(string):
    opening_brace = 0
    closing_brace = 0
    nest = 0

    kims = re.findall(r'\{\w*\}', string, re.I)
    print(kims)

    # for char in string:
    #     if char == '{':
    #         opening_brace += 1
    #     elif char == '}':
    #         closing_brace += 1
    #
    #     if closing_brace > opening_brace:
    #         return -1
    #
    # if closing_brace != opening_brace:
    #     return -1


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
