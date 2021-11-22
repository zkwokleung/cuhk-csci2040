import os

# Exercise 1

from p2 import roman_to_decimal
print('Load p2.py')
expected = [68, 1373, 1690, -1]
test_case = [['XXIV', 'XLIV'], ['XLIX', 'MCCCXXIV'], ['MCCXXXIV', 'CDLVI'], ['MMMMMMMMMM','MXCVI']]

print('Testing...')
answer = list(map(roman_to_decimal, test_case))
if answer == expected:
    print("You passed all the tests!")
else:
    print("Wrong answer, you failed the tests!")
