fib1 = 1
fib2 = 2
total = 0

while fib1 < 4000000:
	if fib1 % 2 == 0:
		total += fib1
	temp = fib1
	fib1 = fib2
	fib2 = temp + fib2

print total