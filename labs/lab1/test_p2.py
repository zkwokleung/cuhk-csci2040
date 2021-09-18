import pexpect

ok = 0

child = pexpect.spawn('python3 p2.py')

child.sendline('210')
child.readline()

child.sendline('012')
test1 = child.readline().rstrip()
print(test1)
cmp_str = 'I do not understand what you mean! Say again: 012'
if (test1 == cmp_str or test1.decode() == cmp_str):
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')


child.sendline('010')
test2 = child.readline().rstrip()
print(test2)
cmp_str = 'I do not understand what you mean! Say again: 010'
if (test2 == cmp_str or test2.decode() == cmp_str):
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')

child.sendline('NB aA  bn')
test3 = child.readline().rstrip()
print(test3)
cmp_str = 'No BRIBING as I am loyal to the King!: NB aA  bn'
if (test3 == cmp_str or test3.decode() == cmp_str):
	print ('TEST 3 OK!')
	ok += 1
else:
	print ('TEST 3 FAIL.')

child.sendline('NB aA bn')
test4 = child.readline().rstrip()
print(test4)
cmp_str = 'I do not understand what you mean! Say again: NB aA bn'
if (test4 == cmp_str or test4.decode() == cmp_str):
	print ('TEST 4 OK!')
	ok += 1
else:
	print ('TEST 4 FAIL.')

test5 = child.readline().rstrip()
print(test5)
cmp_str = 'Welcome to the wonderland!'
if (test5 == cmp_str or test5.decode() == cmp_str):
	print ('TEST 5 OK!')
	ok += 1
else:
	print ('TEST 5 FAIL.')

if ok == 5:
	print ('You pass all the tests!')
