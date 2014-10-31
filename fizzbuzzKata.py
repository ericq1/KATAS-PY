def fizzbuzz(num):
	isDiv3 = False
	isDiv5 = False
	ret = ''
	if num % 3 == 0:
		isDiv3 = True
	if num % 5 == 0:
		isDiv5 = True
	if isDiv3:
		if isDiv5:
			return 'fizzbuzz'
		else:
			return 'fizz'
	elif isDiv5:
		return 'buzz'
	else:
		return str(num)

def test_to_roman():  
	assert foo(1)==   '1'
	assert     foo(2)  == '2'
	assert    foo(3)  == 'fizz'
	assert    foo(4)  == '4'
	assert    foo(5)  == 'buzz'
	assert    foo(6)  == 'fizz'
	assert    foo(10) == 'buzz'
	assert    foo(15) == 'fizzbuzz'
	raise NotImplementedError
