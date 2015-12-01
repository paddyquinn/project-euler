import math

def numFactors(x):
	factors = 0
	i = 1
	while i < math.ceil(math.sqrt(x)):
		if x % i == 0:
			if x / i != i:
				factors += 2
			else:
				factors += 1
		i += 1
	return factors

def main():
	triangle = 36
	factors = 6
	i = 8
	while factors <= 500:
		factors = numFactors(triangle)
		i += 1
		triangle += i
	print triangle - i

main()