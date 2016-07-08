data = [6, 4, 19, 14, 2, 0, 1, 9, 10, 16, 12, 3, 7]
#data = [10, 16, 12, 3, 7]
data = list(reversed(data))
linelist = []


print("Your last 10 scores were:")

if len(data) >= 10:
	for i in range(10):
		if data[i] < 10:
			line = " Game {}: {}   {}".format(i+1, data[i], "#"*data[i]) if i<9 else "Game {}: {}   {}".format(i+1, data[i], "#"*data[i])
		else:
			line = " Game {}: {}  {}".format(i+1, data[i], "#"*data[i]) if i<9 else "Game {}: {}  {}".format(i+1, data[i], "#"*data[i])
		linelist.append(line)
else:
	print("You need to have played more than 10 games to see this!")

print("\n".join(linelist))
