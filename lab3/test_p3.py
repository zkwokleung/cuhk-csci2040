import os

if os.path.isfile('p3.py'):
    try:
        from p3 import load_data
        print('Successfully load p3.py and function load_data(), we will manually grade the function')
    except:
        print('Cannot load query_following, please check the function name or syntax')

    try:
        from p3 import most_follower
        print('Successfully load p3.py and function most_follower()')
        expected = ['Rachel Taylor', 'Vivian Rodriquez', 'Laveta Henderson', 'Lewis Stowers', 'Walter Mckinley', 'Lynn Beasley', 'Steven Marks', 'John Brumfield', 'Christopher Mcintire', 'Amina Rodriguez', 'Stacy Carney', 'Lawrence Whitt', 'Andrew Matos', 'Ruben Weiner', 'Sandy Felts', 'Hannah Jensen', 'Anthony Rivera', 'Kurt Marschke', 'James Harness', 'Peter Pichardo', 'Wilber Roberts', 'Alex Mcdonald', 'Chet Pierre', 'Denise Rodriguez', 'Christopher Reed', 'Linda Addison', 'Deirdre Young', 'Rosalyn Newnam', 'Theresa Walling', 'Sophia Farrington', 'Troy Robichaux', 'Norma Beato', 'Kristen Brown', 'Sean Rivera', 'Joseph Morton', 'Gerald Austerberry', 'Edna Price', 'Michael Gonzalez', 'Doris Moody', 'Brandon Roberson', 'Maria Wesley', 'Christine Bachman', 'Helen Head', 'Curtis Bush', 'Frank Smith', 'Sherri Ryan', 'Victor Bray', 'Gerda Dominguez', 'Mary Craft', 'Shemeka Hammond', 'Jerry Bowe', 'Betty Gebhard', 'Hannah Winfield', 'Martha Bruno', 'Toby Alzate', 'Christine Phillips', 'Jerome Martinez', 'Joyce Rhoads', 'Gloria Earl', 'Richard Neptune', 'Debbie Duncan', 'Dorothy Chunn', 'Patricia Ray', 'Martin Stewart', 'Danny Green', 'Dawn Conti', 'Sharon Bruce', 'Marie Turpin', 'Aaron Moulton', 'Margaret Huett', 'Ann Gambles', 'Stephen Gillis', 'Sheena Payne', 'Joe Sinkler', 'Jake Williams', 'James Hunt', 'David Lessman', 'Barbara Fitch', 'David Green', 'Joseph Carrillo', 'Jenny Stringer', 'Mark Adams', 'Betty Hertler', 'Ricardo Martinez', 'Nancy Youngblood', 'Leona Mccarty', 'Anthony Talton', 'Jonathan Bentz', 'Jeffrey Kelley', 'Alicia Wesson', 'Modesta Salas', 'Richard White', 'Rebekah Harpster', 'Sherry Rubottom', 'Donald Linden', 'Teresa Nelsen', 'Cleo Huber', 'Cathy Yerkes', 'Nicholas Scarbrough', 'Jack Ray', 'William Bledsoe', 'Brian Dierking', 'Mayra Pierro', 'James Teague', 'Deloise Comacho', 'Wendy Grimes', 'Roger Galvin', 'Dorothy Mendez', 
'Cassie Knight', 'Gloria Hoffpauir', 'Gertrude Paschal', 'Samuel Coulston', 'Henry Pileggi']
        try:
            print('Testing...')
            answer = most_follower(load_data('followers.pydata'))
            if answer == expected:
                print('You passed the tests!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except:
            print('Runtime error when testing most_follower, please check your code')
    except:
        print('Cannot load most_follower, please check the function name or syntax')

    try:
        from p3 import update
        print('Successfully load p3.py and function update(), we will manually grade the function')
    except:
        print('Cannot load update, please check the function name or syntax')

    try:
        from p3 import get_num_of_followers
        print('Successfully load p3.py and function get_num_of_followers()')
        test_case = ['Laura Murray', 'Theresa Vale', 'Anne Smelcer']
        expected = [80, 36, 3]

        try:
            print('Testing...')
            answer_dict = get_num_of_followers()
            answer = [answer_dict[name] for name in test_case]
            if answer == expected:
                print('You passed the tests!')
            else:
                print('Wrong result!')
        except:
            print('Runtime error when testing get_num_of_followers, please check your code')
    except:
        print('Cannot load get_num_of_followers, please check the function name or syntax')

else:
    print("Cannot find p3.py, please put p3.py and this test script in the same folder.")
