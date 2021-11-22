import pexpect

ok = 0

child = pexpect.spawn('python3 p4.py')

child.sendline('A-, 3')
child.readline()
test1 = child.readline()
print(test1)
current_gpa = float(test1.split()[2])
if current_gpa == 3.7:
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')

child.sendline('B+, 2')
child.readline()
test2 = child.readline()
print(test2)
current_gpa = float(test2.split()[2])
if current_gpa == 3.54:
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')

child.sendline('C, -2')
child.readline()
test3 = child.readline().rstrip()
print(test3)
if(test3 == 'Wrong input!' or test3.decode() == 'Wrong input!'):
    print ('TEST 3 OK!')
    ok += 1
else:
    print ('TEST 3 FAIL.')

child.sendline('G, 4')
child.readline()
test4 = child.readline().rstrip()
print(test4)
if(test4 == 'Wrong input!' or test4.decode() == 'Wrong input!'):
    print ('TEST 4 OK!')
    ok += 1
else:
    print ('TEST 4 FAIL.')

child.sendline('exit')
child.readline()
test5 = child.readline().rstrip()
print(test5)
if (test5 == 'Your GPA: 3.54.' or test5.decode() == 'Your GPA: 3.54.'):
	print ('TEST 5 OK!')
	ok += 1
else:
	print ('TEST 5 FAIL.')

test6 = child.readline().rstrip()
print(test6)
if (test6 == 'Program ends.' or test6.decode() == 'Program ends.'):
	print ('TEST 6 OK!')
	ok += 1
else:
	print ('TEST 6 FAIL.')

if ok == 6:
	print ('You pass all the tests!')
