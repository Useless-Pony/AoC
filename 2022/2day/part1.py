#example input used to test basics
input = """A Y
B X
C Z
"""

with open("part1.input") as i:
        input=i.read()

#moves, outcome = dict(zip(list("ABCXYZ"),[1,2,3,1,2,3])), [3,0,6]
moves, outcome = dict(zip(list("ABCXYZ"),[1,2,3,-1,0,1])), [3,6,0]

ends =[]
for i in input[:-1].split("\n"):
	print(i)
#	t = moves[i[0]]-moves[i[2]]
	t = (moves[i[0]]+moves[i[2]])%3
	print(t)
#	e = [outcome[t],moves[i[2]]]
	e = [outcome[moves[i[2]]],t if t else 3]
	ends.append(e)

print(sum([sum(i) for i in ends]))
