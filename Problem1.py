i = 3
x = 3
y = 5
total = 0

while i < 1000:
	if i % x == 0 or i % y == 0:
		total += i
	i += 1

print total