#example input used to test basics
inputs =["""
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""[1:-1]]

#with open("part1.input") as i:
 #       inputs.append(i.read()[:-1])


for input in inputs:
	print("##part1")

	SIZE=1000
	board = [[0 for item in range(SIZE)] for row in range(SIZE)]
	board[0][0]= 1
	T, H, X, Y = [0,0], [0,0], 0, 1
	for line in input.splitlines():
		move = [line[0], int(line.split()[1])]
		for i in range(move[-1]):
			if move[0] == "U":
				H[X] = H[X]+1
				if abs(H[X]-T[X]) > 1:
					T = [H[X]-1, H[Y]]
			if move[0] == "D":
				H[X] = H[X]-1
				if abs(H[X]-T[X]) > 1:
					T = [H[X]+1, H[Y]]
			if move[0] == "L":
				H[Y] = H[Y]-1
				if abs(H[Y]-T[Y]) > 1:
					T = [H[X], H[Y]+1]
			if move[0] == "R":
				H[Y] = H[Y]+1
				if abs(H[Y]-T[Y]) > 1:
					T = [H[X], H[Y]-1]
			board[T[X]][T[Y]] = 1
	print(sum([sum(row) for row in board]))

	print("##part2")

print("done")
