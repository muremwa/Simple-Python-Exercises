# Q4a) Write a function that returns product of all numbers of a list
def product(nums):
    result = 1
    for item in nums:
        result *= item

    return result


def product_recursion(nums):
    if len(nums) < 2:
        return nums[0]

    return nums[0] * product_recursion(nums[1:])


print(product([1, 4, 21]))
print(product_recursion([1, 4, 21]))
# 84
print(product([-4, 2.3e12, 77.23, 982, 0b101]))
print(product_recursion([-4, 2.3e12, 77.23, 982, 0b101]))
# -3.48863356e+18
print(product((-3, 11, 2)))
# product_recursion(product_recursion((-3, 11, 2)))
# -66
print(product({8, 300}))
# print(product_recursion({8, 300}))
# 2400
print(product([234, 121, 23, 945, 0]))
# 0
print(product(range(2, 6)))
print(product_recursion(range(2, 6)))
# 120
# can you identify what mathematical function the last one performs?
