# Q4b) Write a function that returns nth lowest number of a list (or iterable in general).
# Return the lowest if second argument not specified
# Note that if a list contains duplicates, they should be handled before determining nth lowest


def nth_lowest(list_1, nth=1):
    # remove duplicates and sort
    list_1 = list(set(list_1))
    list_1.sort()

    return list_1[nth-1]


nums = [42, 23421341, 234.2e3, 21, 232, 12312, -2343]
print(nth_lowest(nums, 3))
# 42
print(nth_lowest(nums, 5))
# 12312
# print(nth_lowest(nums, 15))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in nth_lowest
# IndexError: list index out of range
#
nums = [1, -2, 4, 2, 1, 3, 3, 5]
print(nth_lowest(nums))
# -2
print(nth_lowest(nums, 4))
# 3
print(nth_lowest(nums, 5))
# 4
#
print(nth_lowest('unrecognizable', 3))
# 'c'
print(nth_lowest('abracadabra', 4))
# 'd'
