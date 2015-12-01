zero = (0,0,0,3)
one = (1,3,0,6)
two = (2,3,6,6)
three = (3,5,6,8)
four = (4,4,5,8)
five = (5,4,5,7)
six = (6,3,5,7)
seven = (7,5,7,9)
eight = (8,5,6,8)
nine = (9,4,6,8)

ones = [zero,one,two,three,four,five,six,seven,eight,nine]

totalLength = 0
for x in range(999):
	y = str(x+1)
	currentLength = 0
	if len(y) == 3:
		i = 0
		while ones[i][0] != int(y[0]):
			i += 1
		currentLength += ones[i][1]
		currentLength += 7
		if int(y[1]) != 0 or int(y[2]) != 0:
			currentLength += 3
			i = 0
			while ones[i][0] != int(y[1]):
				i += 1
			currentLength += ones[i][2]
			if i == 1:
				i = 0
				while ones[i][0] != int(y[2]):
					i += 1
				currentLength += ones[i][3]
			else:
				i = 0
				while ones[i][0] != int(y[2]):
					i += 1
				currentLength += ones[i][1]
	elif len(y) == 2:
		i = 0
		while ones[i][0] != int(y[0]):
			i += 1
		currentLength += ones[i][2]
		if i == 1:
			i = 0
			while ones[i][0] != int(y[1]):
				i += 1
			currentLength += ones[i][3]
		else:
			i = 0
			while ones[i][0] != int(y[1]):
				i += 1
			currentLength += ones[i][1]
	else:
		i = 0
		while ones[i][0] != int(y[0]):
			i += 1
		currentLength += ones[i][1]
	totalLength += currentLength

totalLength += 11

print totalLength

