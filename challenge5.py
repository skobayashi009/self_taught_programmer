def squaring():
	"""Returns a squared number.

	Args:
	    x(int): an integer.

	Returns:
	    int: x^2
	"""
	x = int(input())
	return x**2

def return_string(s):
	return s

def f(a=0, b=0, c):
	return a * b * c

def g(s):
	try:
		a = float(s)
	except ValueError:
		print("invalid input")

g("Hello")