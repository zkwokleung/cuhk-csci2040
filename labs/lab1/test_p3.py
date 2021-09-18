import pexpect

ok = 0

child = pexpect.spawn('python3 p3.py')

child.sendline('4')
child.readline()

child.sendline('1')
child.readline()

flag = True
line1 = child.readline().rstrip()
line2 = child.readline().rstrip()
line3 = child.readline().rstrip()
line4 = child.readline().rstrip()
if line1.decode() != '   1' or line2.decode() != '  111' or line3.decode() != ' 11111' or line4.decode() != '1111111':
	flag = False
if (flag == True):
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')


child.sendline('2')
child.readline()

child.sendline('^_^')
child.readline()

flag = True
line1 = child.readline().rstrip()
line2 = child.readline().rstrip()
if line1.decode() != '   ^_^' or line2.decode() != '^_^^_^^_^':
	flag = False
if (flag == True):
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')


child.sendline('-1')
child.readline()
test3 = child.readline().rstrip()
print(test3)
if (test3 == 'Program ends.' or test3.decode() == 'Program ends.'):
	print ('TEST 3 OK!')
	ok += 1
else:
	print ('TEST 3 FAIL.')


if ok == 3:
	print ('You pass all the tests!')
