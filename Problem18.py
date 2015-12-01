levels = []
zero="75"
levels.append(zero.split())
one="95 64"
levels.append(one.split())
two="17 47 82"
levels.append(two.split())
three="18 35 87 10"
levels.append(three.split())
four="20 04 82 47 65"
levels.append(four.split())
five="19 01 23 75 03 34"
levels.append(five.split())
six="88 02 77 73 07 63 67"
levels.append(six.split())
seven="99 65 04 28 06 16 70 92"
levels.append(seven.split())
eight="41 41 26 56 83 40 80 70 33"
levels.append(eight.split())
nine="41 48 72 33 47 32 37 16 94 29"
levels.append(nine.split())
ten="53 71 44 65 25 43 91 52 97 51 14"
levels.append(ten.split())
eleven="70 11 33 28 77 73 17 78 39 68 17 57"
levels.append(eleven.split())
twelve="91 71 52 38 17 14 91 43 58 50 27 29 48"
levels.append(twelve.split())
thirteen="63 66 04 68 89 53 67 30 73 16 69 87 40 31"
levels.append(thirteen.split())
fourteen="04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
levels.append(fourteen.split())

m = 0
while m < 15:
	n = 0
	while n < len(levels[m]):
		levels[m][n] = int(levels[m][n])
		n += 1
	m += 1

i = 1
while i < 15:
	j = 0
	while j < len(levels[i]):
		if j == 0:
			levels[i][j] += levels[i-1][j]
		elif j == len(levels[i]) - 1:
			levels[i][j] += levels[i-1][j-1]
		else:
			temp = [levels[i-1][j-1],levels[i-1][j]]
			levels[i][j] += max(temp)
		j += 1
	i += 1


print max(levels[14])




