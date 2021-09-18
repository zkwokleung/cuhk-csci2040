import pexpect

ok = 0

child = pexpect.spawn('python3 p1.py')

child.sendline('1')
child.readline()

child.sendline('abc')
child.readline()
test0 = child.readline().rstrip()
print(test0)
if (test0 == 'Your input is not an integer!' or test0.decode() == 'Your input is not an integer!'):
	print ('TEST 0 OK!')
	ok += 1
else:
	print ('TEST 0 FAIL.')

child.sendline('10.3')
child.readline()
test1 = child.readline().rstrip()
print(test1)
if (test1 == 'Your input is not an integer!' or test1.decode() == 'Your input is not an integer!'):
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')

child.sendline('2')
child.readline()

child.sendline('10')
child.readline()
test2 = child.readline().rstrip()
print(test2)
value = float(test2.split()[3])

if (value == 4):
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')

test3 = child.readline().rstrip()
print(test3)
if (test3 == 'Program ends.' or test3.decode() == 'Program ends.'):
	print ('TEST 3 OK!')
	ok += 1
else:
	print ('TEST 3 FAIL.')

if ok == 4:
	print ('You pass all the tests!')
