import os

# Exercise 2
if (os.path.isfile('p3.py')):
    try:
        from p3 import reverse
        print('Load p3.py')
        test1 = ['apple']
        test2 = ['abcde']
        expected = [['elppa'], ['edcba']]
        answer=[]
        try:
            print('Testing...')
            answer.append(list(map(reverse, test1)))
            answer.append(list(map(reverse,test2)))
            if answer == expected:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing fibo, please check your code!')
    except:
        print('Cannot load fibo, please check the function name or syntax.')
else:
    print('Cannot find p3.py, please put p3.py and this test script in the same folder.')
