def chainLength(x):
	length = 1
	while x > 1:
		if x % 2 == 0:
			x /= 2
		else:
			x *= 3
			x += 1
		length += 1
	return length

def main():
	maxLength = 0
	maxStart = 0
	x = 1
	while x < 1000000:
		currentLength = chainLength(x)
		if currentLength > maxLength:
			maxLength = currentLength
			maxStart = x
		x += 1
	print maxStart

main()