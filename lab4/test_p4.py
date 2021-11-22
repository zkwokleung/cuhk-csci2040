import os

if os.path.isfile('p4.py'):
    try:
        from p4 import get_final_grades
        print('Successfully load p4.py')
        expected = [42.875, 58.15, 37.875, 89.275, 98.7]
        try:
            print('Testing...')
            test_case = ['SID1155000001', 'SID1155000002', 'SID1155000003','SID1155000150','SID1155000200']
            answer_dict = get_final_grades('grades.csv')
            answer = [answer_dict[name] for name in test_case]
            if answer == expected:
                print('You passed all the tests!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except Exception as e:
            print('Runtime error when testing get_final_grades, the error message is as follows:')
            print (e)
    except:
        print('Cannot load get_final_grades, please check the function name or syntax')
else:
    print("Cannot find p4.py, please put p4.py and this test script in the same folder.")


