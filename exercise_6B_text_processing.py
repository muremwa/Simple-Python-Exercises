# Q6b) Check if a word is in ascending/descending alphabetic order or not (irrespective of case)
#
# Can you think of a way to do it only using built-in functions and string methods?


def is_alpha_order(string):
    string_case = list(string.lower())
    string_case.sort()
    string_case_op = string_case.copy()
    string_case_op.sort(reverse=True)

    if list(string.lower()) == string_case:
        return True
    elif list(string.lower()) == string_case_op:
        return True
    else:
        return False


# bonus: Check if all words in a sentence (assume only whitespace separated input) are in ascending/descending
# alphabetic order (irrespective of case)
#
# hint use a built-in function and generator expression


def sentence_separator(sent):
    for word in sent.split(' '):
        yield word


def is_alpha_order_sentence(sentence):
    counter = 0
    for s in sentence_separator(sentence):
        if not is_alpha_order(s):
            counter += 1

    if counter == 0:
        return True
    else:
        return False


print(is_alpha_order('bot'))
# True
print(is_alpha_order('arT'))
# True
print(is_alpha_order('are'))
# False
print(is_alpha_order('boat'))
# False
print(is_alpha_order('toe'))
# True
print(is_alpha_order('Flee'))
# False
print(is_alpha_order('reed'))
# True
print(is_alpha_order_sentence('Toe got bit'))
# True
print(is_alpha_order_sentence('All is well'))
# False
