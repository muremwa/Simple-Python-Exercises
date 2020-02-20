# Q4c) Write a function that accepts a string input and returns slices
#
# if input string is less than 3 characters long, return a list with input string as the only element
# otherwise, return list with all string slices greater than 1 character long
# order of slices should be same as shown in examples below


def word_slices(string):
    # less than 3 characters
    if len(string) < 3:
        return [string]

    # more than 3 characters
    splice = []
    for c, l in enumerate(string):
        for k, nl in enumerate(string[c+1:]):
            splice.append(l+string[c+1:][:k+1])

    return splice


print(word_slices('i'))
# ['i']
print(word_slices('to'))
# ['to']
#
print(word_slices('are'))
# ['ar', 'are', 're']
print(word_slices('table'))
# ['ta', 'tab', 'tabl', 'table', 'ab', 'abl', 'able', 'bl', 'ble', 'le']
print(word_slices('muremwa'))
