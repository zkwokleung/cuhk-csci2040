import os

if os.path.isfile('p1.py'):
    try:
        from p1 import list1
        print('Successfully load list1')
        expected1 = ['SEDAN', 'SUV', 'MINIVAN', 'VAN', 'BICYCLE', 'MOTORCYCLE']
        try:
            print('Testing...')
            if list1 == expected1:
                print('You passed the first test!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except Exception as e:
            print('Error when testing list1, the error message is as follows:')
            print (e)
    except:
        print('Cannot load list1, please check the function name or syntax')

    try:
        from p1 import list2
        print('Successfully load list2')
        expected2 = ['1*1=1', '1*2=2 2*2=4', '1*3=3 2*3=6 3*3=9', '1*4=4 2*4=8 3*4=12 4*4=16', '1*5=5 2*5=10 3*5=15 4*5=20 5*5=25', '1*6=6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36', '1*7=7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49', '1*8=8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64', '1*9=9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81']
        try:
            print('Testing...')
            if list2 == expected2:
                print('You passed the second test!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except Exception as e:
            print('Error when testing list2, the error message is as follows:')
            print (e)
    except:
        print('Cannot load list2, please check the function name or syntax')

    try:
        from p1 import list3
        print('Successfully load list3')
        expected3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        try:
            print('Testing...')
            if list3 == expected3:
                print('You passed the third test!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except Exception as e:
            print('Runtime error when testing list3, the error message is as follows:')
            print (e)
    except:
        print('Cannot load list3, please check the function name or syntax')

    try:
        from p1 import list4
        print('Successfully load list4')
        expected4 = [2, 4, 6, 8, 10]
        try:
            print('Testing...')
            if list4 == expected4:
                print('You passed the fourth test!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except Exception as e:
            print('Runtime error when testing list4, the error message is as follows:')
            print (e)
    except:
        print('Cannot load list4, please check the function name or syntax')

    try:
        from p1 import dict5
        print('Successfully load p1.py')
        expected5 = {'apple': 37.0, 'pear': 51.0, 'banana': 82.0, 'strawberry': 63.0}
        expected55 = {'apple': 37, 'pear': 51, 'banana': 82, 'strawberry': 63}
        try:
            print('Testing...')
            if dict5 == expected5 or dict5 == expected55:
                print('You passed the fifth test!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except Exception as e:
            print('Error when testing dict5, the error message is as follows:')
            print (e)
    except:
        print('Cannot load dict5, please check the function name or syntax')

else:
    print("Cannot find p1.py, please put p1.py and this test script in the same folder.")


