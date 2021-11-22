import os

# Exercise 4
if (os.path.isfile('p1.py')):
    try:
        from p1 import check_sublist
        print('Load p1.py')
        test1 = [[25,331,422,6,3,10]]
        test2 = [8]
        test3 = [2]
        test4=[12]
        expected = [([25, 331, 422], [331, 422], [6, 3, 10])]
        try:
            print('Testing...')
            answer = list(map(check_sublist, test1, test2, test3,test4))
            print(answer)
            if answer == expected:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing check_sublist, please check your code!')
    except:
        print('Cannot load check_sublist, please check the function name or syntax.')
else:
    print('Cannot find p1.py, please put p1.py and this test script in the same folder.')
