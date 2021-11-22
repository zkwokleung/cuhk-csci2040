import pexpect

ok = 0

child = pexpect.spawn('python3 p5.py')

child.sendline('2 8')
test1 = child.readline().rstrip()
cmp_str = 'Please input goal posts:'
print(test1)
if (test1 == cmp_str or test1.decode() == cmp_str):
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')

child.sendline('0')
child.readline()
test2 = child.readline().rstrip()
print(test2)
cmp_str = 'You missed!'
if (test2 == cmp_str or test2.decode() == cmp_str):
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')


child.sendline('5')
child.readline()
test3 = child.readline().rstrip()
print(test3)
cmp_str = 'Goal!'
if (test3 == cmp_str or test3.decode() == cmp_str):
	print ('TEST 3 OK!')
	ok += 1
else:
	print ('TEST 3 FAIL.')

child.sendline('5')
child.readline()
test4 = child.readline().rstrip()
print(test4)
cmp_str = 'Goal!'
if (test4 == cmp_str or test4.decode() == cmp_str):
	print ('TEST 4 OK!')
	ok += 1
else:
	print ('TEST 4 FAIL.')

child.sendline('8')
child.readline()
test5 = child.readline().rstrip()
print(test5)
cmp_str = 'Top Bin!!!'
if (test5 == cmp_str or test5.decode() == cmp_str):
	print ('TEST 5 OK!')
	ok += 1
else:
	print ('TEST 5 FAIL.')

child.sendline('20')
child.readline()
test6 = child.readline().rstrip()
print(test6)
cmp_str = 'You missed!'
if (test6 == cmp_str or test6.decode() == cmp_str):
	print ('TEST 6 OK!')
	ok += 1
else:
	print ('TEST 6 FAIL.')

test7 = child.readline().rstrip()
print(test7)
cmp_str = 'Finished with 2 goals and 1 top bin.'
if (test7 == cmp_str or test7.decode() == cmp_str):
	print ('TEST 7 OK!')
	ok += 1
else:
	print ('TEST 7 FAIL.')

test8 = child.readline().rstrip()
print(test8)
cmp_str = 'Your final score is 4.'
if (test8 == cmp_str or test8.decode() == cmp_str):
	print ('TEST 8 OK!')
	ok += 1
else:
	print ('TEST 8 FAIL.')

test9 = child.readline().rstrip()
print(test9)
cmp_str = 'Program ends.'
if (test9 == cmp_str or test9.decode() == cmp_str):
	print ('TEST 9 OK!')
	ok += 1
else:
	print ('TEST 9 FAIL.')

if ok == 9:
	print ('You pass all the tests!')