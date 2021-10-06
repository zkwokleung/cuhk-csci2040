import os

# Exercise 1

if (os.path.isfile('p2.py')):
    try:
        from p2 import roman_to_decimal
        print('Load p2.py')
        expected = [[68], [1373], [1690], [-1]]
        answer=[]
        test_case = [[['XXIV'], ['XLIV']], [['XLIX'], ['MCCCXXIV']], [['MCCXXXIV'], ['CDLVI']], [['MMMMMMMMMM'],['MXCVI']]]
        length=len(test_case)
        try:
            print('Testing...')
            for i in range(length):
                answer.append(list(map(roman_to_decimal,test_case[i][0],test_case[i][1])))
            if answer == expected:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing roman_to_decimal, please check your code!')
    except:
        print('Cannot load roman_to_decimal, please check the function name or syntax.')
else:
    print('Cannot find p2.py, please put p2.py and this test script in the same folder.')
