# Q5b) Print sum of all numbers (assume only positive integer numbers) from a file containing arbitrary string
import re


def main():
    # open file and copy all text
    with open('files/f2.txt', 'r') as f:
        text = f.read()

    # search for number sequences in the text using regular expressions
    nums = re.findall(r'\d+', text, re.I | re.M)

    # add all numbers and return result
    nums = [int(num) for num in nums]
    total = 0
    for num in nums:
        total += int(num)

    print(total)


if __name__ == '__main__':
    main()
