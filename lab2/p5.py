def count_alphabet(test_string):
    # print(''.join([c for c in test_string.lower() if c.isalpha()]))
    return len(''.join([c for c in test_string.lower() if c.isalpha()]))


def hk_capitalization(test_string):
    return ''.join([c if c != 'h' and c != 'k' else c.upper() for c in test_string])


def concat(test_string, new_string):
    return str(test_string) + str(new_string)


def search(test_string: str, sub):
    return test_string.rfind(sub)


def letter_count(test_string):
    temp = {}
    for c in test_string.lower():
        if c.isalpha():
            if c in temp:
                temp[c] += 1
            else:
                temp[c] = 1
    return sorted([(k, temp[k]) for k in temp], key=lambda x: x[0])


if __name__ == '__main__':
    ipt1 = input("str1: ")
    ipt2 = input("str2: ")
    # print("count_alphabet: " + str(count_alphabet(ipt1)))
    # print("hk_capitalization: " + hk_capitalization(ipt1))
    # print("concat: " + concat(ipt1, ipt2))
    pass
