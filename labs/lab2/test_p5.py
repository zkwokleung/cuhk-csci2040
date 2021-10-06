import os

# Exercise 5
if (os.path.isfile('p5.py')):
    try:
        import p5
        print('Load p5.py')
        try:
            print('Testing...')
            test_string = 'Alice was born in 1996 and born in hong kong.'
            test_count_string = ['This is a test! Just Write somEthIng RAndOmlY123',
                     'The quick brown fox jumps over the lazy dog',
                     'CSCI2040--Introduction to Python',
                     'Teacher: Prof. John C.S. Lui',
                     'Have fun!']
            actual_ans = []
            actual_ans.append(p5.count_alphabet(test_string))
            actual_ans.append(p5.hk_capitalization(test_string))
            actual_ans.append(p5.concat(test_string, ' She is 22 now.'))
            actual_ans.append(p5.search(test_string, 'born'))
            actual_ans.append(p5.search(test_string, 'now'))
            actual_ans = actual_ans + list(map(p5.letter_count, test_count_string))
            expected_ans = [31, 'Alice was born in 1996 and born in Hong Kong.',
                            'Alice was born in 1996 and born in hong kong. She is 22 now.', 27, -1, [('a', 2), ('d', 1), ('e', 3), ('g', 1), ('h', 2), ('i', 4), ('j', 1), ('l', 1), ('m', 2), ('n', 2), ('o', 2), ('r', 2), ('s', 5), ('t', 6), ('u', 1), ('w', 1), ('y', 1)], [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 3), ('f', 1), ('g', 1), ('h', 2), ('i', 1), ('j', 1), ('k', 1), ('l', 1), ('m', 1), ('n', 1), ('o', 4), ('p', 1), ('q', 1), ('r', 2), ('s', 1), ('t', 2), ('u', 2), ('v', 1), ('w', 1), ('x', 1), ('y', 1), ('z', 1)], [('c', 3), ('d', 1), ('h', 1), ('i', 3), ('n', 3), ('o', 4), ('p', 1), ('r', 1), ('s', 1), ('t', 4), ('u', 1), ('y', 1)], [('a', 1), ('c', 2), ('e', 2), ('f', 1), ('h', 2), ('i', 1), ('j', 1), ('l', 1), ('n', 1), ('o', 2), ('p', 1), ('r', 2), ('s', 1), ('t', 1), ('u', 1)], [('a', 1), ('e', 1), ('f', 1), ('h', 1), ('n', 1), ('u', 1), ('v', 1)]]
            if actual_ans == expected_ans:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing TextProcessor, please check your code!')
    except:
        print('Cannot load TextProcessor, please check the class name or syntax.')
else:
    print('Cannot find p5.py, please put p5.py and this test script in the same folder.')
