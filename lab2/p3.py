def reverse(str):
    if len(str) > 0:
        return reverse(str[1:]) + str[0]
    else:
        return str