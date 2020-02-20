# accepts a filesystem path(default) or a url(indicated by True as second argument)
# returns the longest word(here word is defined as one or more consecutive sequence of alphabets of either case)
# assume that input encoding is utf-8 and small enough to fit in memory and that there's only one distinct longest word
import string


def longest_word(*args):
    path = args[0]
    try:
        url = args[1]
    except IndexError:
        pass

    with open(path, 'r') as f:
        words = f.read()

    words = words.split("\n")
    # remove all punctuation
    words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]
    words = [word.split(" ") for word in words]
    x = []
    for word_list in words:
        x = x + word_list

    return sorted(x, key=len, reverse=True)[0]


ip_path = 'files/poem.txt'
print(longest_word(ip_path))
# 'Violets'
