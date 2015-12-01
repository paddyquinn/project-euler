import math

def isPrime(x):
	if x % 2 == 0:
		return False
	else:
		i = 3
		while i <= math.ceil(math.sqrt(x)):
			if x % i == 0:
				return False
			i += 2
		return True

def main():
	numPrimes = 6
	current = 13

	while numPrimes < 10001:
		current += 2
		if isPrime(current):
			numPrimes += 1

	print current

main()