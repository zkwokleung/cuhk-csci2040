import os
import math

# Exercise 5
if (os.path.isfile('p4.py')):
    try:
        from p4 import *
        print('Load p4.py')
        # test input
        triangles = [(3,4,5),(3,6,1)]

        # expected answers
        expected_ans = [True,
                        6.0,
                        12,
                        True]
        try:
            print('Testing...')
            actual_ans = []
            # test case 1: (5, 5, 6)
            actual_ans.append(is_right_triangle(triangles[0]))

            # test case 2: area of (5, 5, 6)
            actual_ans.append(area(triangles[0]))

            # test case 3: perimeter of (5, 5, 6)
            actual_ans.append(perimeter(triangles[0]))

            # test case 4: (10, 10, 8)
            actual_ans.append(check_invalid(triangles[1]))

            if actual_ans == expected_ans:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing triangle, please check your code!')
    except:
        print('Cannot load triangle, please check the class name or syntax.')
else:
    print('Cannot find p4.py, please put p4.py and this test script in the same folder.')
