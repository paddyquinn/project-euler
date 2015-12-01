import math

def lowestFactor(x):
	if x % 2 == 0 and x != 2:
		return x/2
	else:
		i = 3
		while i <= math.ceil(math.sqrt(x)):
			if x % i == 0:
				return i
			i += 2
		return x

def factor(x, pF):
	y = lowestFactor(x)
	if y != x:
		factor(y, pF)
		factor(x/y, pF)
	else:
		pF.append(y)

def main():
	number = 600851475143
	primeFactorization = []
	factor(number, primeFactorization)
	print max(primeFactorization)

main()