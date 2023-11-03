def add(*args):
	total = 0
	print(args)
	for n in args:
		total += n
	return total

def calculate(n, **kwargs):
	n += kwargs["add"]
	n *= kwargs["multiply"]
	print(n)

calculate(2, add=3, multiply=3)

