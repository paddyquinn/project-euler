def isPalindrome(x):
	y = str(x)
	i = 0
	j = len(y) - 1
	while i < j:
		if y[i] == y[j]:
			i += 1
			j -= 1
		else:
			return False
	return True

def main():
	maximum = 0
	x = 100
	while x < 1000:
		y = x
		while y < 1000:
			product = x*y
			if isPalindrome(product):
				if product > maximum:
					maximum = product
			y += 1
		x += 1
	print maximum

main()