# utils.py
from scipy import integrate as int

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	return 1 if (n==1 or n==0) else n * fact(n - 1)

	pass

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	ro = b*b-(4*a*c)
	r1 = (-b+ro**(0.5))/(2*a)
	r2 = (-b-ro**(0.5))/(2*a)
	return (r1,r2)
	pass

def integrate(function, lower, upper):
	
	y , err = int.quad(function, lower, upper)
	return y
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
