"""
Think Python CH 5.8 Run through
"""

def countdown(n):
	"""Counting a function within itself"""
	if n <= 0:
		print 'Blastoff!'
	else:
		print n
		countdown(n-1)

#countdown(10)

def print_n(s,n):
	if n <= 0:
		return
	print s
	print_n(s,n-1)

#print_n(5,5)

"""
Think Python CH 6.5 Run through
"""
def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n* recurse
		return result

#print factorial(1.5)

def fibonacci(n):
	if n==0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

#print fibonacci(1.5)

def factorial2(n):
	if not isinstance(n, int):
		print 'Factorial is only defined for integers.'
		return None
	elif n<0:
		print "Factorial is not defined for negative integers."
		return None
	elif n == 0:
		return 1
	else:
		return n * factorial(n-1)

factorial2(-2)

