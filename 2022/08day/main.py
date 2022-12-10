#example input used to test basics
inputs =["""
30373
25512
65332
33549
35390"""[1:]]

with open("part1.input") as i:
        inputs.append(i.read()[:-1])


for input in inputs:
	forest = [[int(tree) for tree in line] for line in input.splitlines()]
	f_forest = list(zip(*forest))
	width = len(forest)
	visible = 0

	print("##part1")
	for x, row in enumerate(forest):
		if (x == 0) or (x == len(row) -1): continue
		for y, tree in enumerate(row):
			if (y == 0) or (y == len(row) -1): continue
			hidden= True
#			print(tree,forest)
			if tree > max(f_forest[y][:x]): hidden = False
			if not hidden:visible += 1; continue

			hidden = True
			if tree > max(f_forest[y][x+1:]): hidden = False
			if not hidden: visible += 1; continue

			hidden= True
#			print(tree,forest)
			if tree > max(forest[x][:y]): hidden = False
			if not hidden:visible += 1; continue

			hidden = True
			if tree > max(forest[x][y+1:]): hidden = False
			if not hidden: visible += 1; continue
#			print("invisible")

	print(width *4 -4 + visible)

	print("##part2")
	scores = [[0 for i in range(width)] for I in range(width)]

	for x, row in enumerate(forest):
		if (x == 0) or (x == len(row) -1): continue
		for y, tree in enumerate(row):
			if (y == 0) or (y == len(row) -1): continue

			down = 0
			up = 0
			right = 0
			left = 0

			for T in f_forest[y][:x][::-1]:
				down += 1
				if T >= tree: break

			for T in f_forest[y][x+1:]:
				up += 1
				if T >= tree: break

			for T in forest[x][:y][::-1]:
				left += 1
				if T >= tree: break

			for T in forest[x][y+1:]:
				right += 1
				if T >= tree: break

			scores[x][y] = left*right*up*down
		#	scores[x][y] = [down,up,left,right]
	print(*scores,sep="\n")
	print(max(*[max(*row) for row in scores]))
print("done")
