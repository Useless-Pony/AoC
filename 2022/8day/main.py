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

print("done")
