# Q5c) Sort file contents in alphabetic order based on each line's extension
#
# extension here is defined as the string after the last . in the line
# if line doesn't have a ., those lines should come before lines with .
# sorting should be case-insensitive
# use rest of string as tie-breaker if there are more than one line with same extension
# assume input file is ASCII encoded and small enough to fit in memory
import re


def main():
    # get all file names
    with open('files/f3.txt', 'r') as f:
        files = [line.strip() for line in f]

    # sort by extension
    exes = [
        re.findall(r'\.(\w+)$', file_name, re.I) for file_name in files
    ]

    files_inn = {}

    for k, eve in enumerate(exes):
        if len(eve) == 0:
            try:
                files_inn['none'].append([files[k], k])
            except KeyError:
                files_inn['none'] = [[files[k], k]]
        else:
            try:
                files_inn[eve[0].upper()].append([files[k], k])
            except KeyError:
                files_inn[eve[0].upper()] = [[files[k], k]]

    for key, value in files_inn.items():
        value.sort()
        files_inn[key] = [name[0] for name in value]

    result = [name for name in files_inn['none']]
    del(files_inn['none'])
    names = list(files_inn)
    names.sort()

    for ex in names:
        for file in files_inn[ex]:
            result.append(file)

    # bonus: instead of printing results to stdout, change the input file itself with sorted result
    with open('files/f3answers.txt', 'w') as f:
        for res in result:
            print(res, file=f)
            print(res)


if __name__ == '__main__':
    main()
