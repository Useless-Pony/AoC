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
## this is all scuffed
	SIZE=5
	LEN=2
	board = [[0 for item in range(SIZE)] for row in range(SIZE)]
	board[0][0] = 1
	X, Y = 0, 1
	moves = {"U":[1, 0], "D":[1, 0], "L":[0, -1], "R":[0, 1]}
	offsets = {
		"[2, 0]":[1, 0], "[-2, 0]":[1, 0], "[0, -2]":[0, -1], "[0, 2]":[0, 1],
		"[2, 1]":[1, 1], "[-2, 1]":[1, 1], "[1, -2]":[1, -1], "[1, 2]":[1, 1],
		"[2, -1]":[1, -1], "[-2, -1]":[1, -1], "[-1, -2]":[-1, -1], "[-1, 2]":[-1, 1]}
	rope = [[0, 0] for i in range(LEN)]
	for line in input.splitlines():
		offset = moves[line[0]]
		move = int(line.split()[1])
		for i in range(move):
#try to not have a special case
#makes first "prev" a ghost knot that pulls the head to where it's supposed to move
			prev_knot = rope[0].copy()
			prev_knot = [sum(itm) for itm in list(zip(prev_knot, offset, offset))]
			prev_pos = []
			for ind,knot in enumerate(rope):
				knot_tmp = knot.copy()

				rel = [prev - cur for prev,cur in zip(prev_knot, knot)]
				print(rel)
				if str(rel) in offsets:
					knot = [knot[X]+offsets[str(rel)][X],
						knot[Y]+offsets[str(rel)][Y]
						]
				print(knot)

				prev_knot = knot
				prev_pos = knot_tmp
			board[rope[LEN-1][X]][rope[LEN-1][Y]] = 1
			print(*board[::-1], sep="\n", end="\n\n")
	print(sum([sum(row) for row in board]))

print("done")
