# Q3a) Write a function that returns
#
#       'Good' for numbers divisible by 7
#       'Food' for numbers divisible by 6
#       'Universe' for numbers divisible by 42
#       'Oops' for all other numbers
#       Only one output, divisible by 42 takes precedence


def six_by_seven(integer):
    if integer % 42 == 0:
        return 'Universe'
    elif integer % 6 == 0:
        return 'Food'
    elif integer % 7 == 0:
        return 'Good'
    else:
        return 'Oops'


# bonus: use a loop to print number and corresponding string for numbers 1 to 100
for i in range(1, 101):
    print(i, six_by_seven(i))


# Q3b) Print all numbers from 1 to 1000 which reads the same in reversed form in both binary and decimal format
def bin_dec(num):
    num_l = ''.join(reversed(str(num)))

    if num_l == str(num):
        num_bin = bin(num)[2:]
        num_bin_rev = ''.join(reversed(num_bin))

        if num_bin == num_bin_rev:
            return True


# bonus: add octal and hexadecimal checks as well
def oct_check(num):
    if bin_dec(num):
        oct_1 = oct(num)[2:]
        oct_1_rev = ''.join(reversed(oct_1))

        if oct_1 == oct_1_rev:
            return True


def hex_check(num):
    if oct_check(num):
        hex_1 = hex(num)[2:]
        hex_1_rev = ''.join(reversed(hex_1))

        if hex_1 == hex_1_rev:
            return True


for i in range(1, 1001):
    if bin_dec(i):
        print(i, bin(i)[2:])

for i in range(1, 1001):
    if oct_check(i):
        print(i, bin(i), oct(i))


for i in range(1, 1001):
    if hex_check(i):
        print(i, bin(i), oct(i), hex(i))
