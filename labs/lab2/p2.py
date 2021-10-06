def roman_to_decimal_single(str):
    dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res, last = 0,0
    for rm in str[::-1]:
        dec = dict_roman[rm]
        if dec < last:
            res -= dec
        else:
            res += dec
        
        last = dec
    
    return res



def roman_to_decimal(str1, str2):
    # if the strings are not empty
    if len(str1) > 0 and len(str2) > 0:
        # roman to decimal
        d1 = roman_to_decimal_single(str1)
        d2 = roman_to_decimal_single(str2)
        
        # if both number are in range
        rg = range(1, 9999)
        if (d1 in rg) and (d2 in rg):
            return d1 + d2
    
    return -1

if __name__ == '__main__':
    str1 = input("str1: ")
    str2 = input("str2: ")
    print("res: {}".format(map(roman_to_decimal, [str1, str2])))