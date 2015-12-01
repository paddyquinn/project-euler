# solution based on Pascal's Triangle

lst = [1, 1]
gridSize = 0
while gridSize < 20:
	temp = [1]
	i = 1
	while i < len(lst):
		temp.append(lst[i] + lst[i-1])
		i += 1
	temp.append(1)
	lst = temp
	if len(lst) % 2 != 0:
		gridSize += 1

print max(lst)