a = 3

while a <= 332:
	b = a + 1
	while b <= 498:
		c = b + 1
		while c <= 993:
			if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
				print a * b * c
			c += 1
		b += 1
	a += 1