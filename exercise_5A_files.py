# Q5a) Print sum of all numbers from a file containing only single column and all numbers
def main():
    total = 0
    # open file and add
    with open('files/f1.txt', 'r') as f:
        for num in f:
            total += eval(num.strip())

    # display result
    print(total)


if __name__ == '__main__':
    main()
