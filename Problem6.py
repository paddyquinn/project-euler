squaresum = 0
sumsquare = 0

for x in range(100):
	squaresum += x + 1
	sumsquare += (x+1) ** 2

squaresum = squaresum ** 2
print squaresum - sumsquare