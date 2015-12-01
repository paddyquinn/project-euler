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
	sumPrimes = 17
	current = 11
	while current < 2000000:
		if isPrime(current):
			sumPrimes += current
		current += 2
	print sumPrimes

main()