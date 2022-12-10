#example input used to test basics
input = """A Y
B X
C Z
"""

with open("part1.input") as i:
        input=i.read()

#one way to calculate outcomes is to use the moves in the guid as numbers and then useing the difference as keys for the outcome..
moves, outcome = dict(zip(list("ABCXYZ"),[1,2,3,1,2,3])), [3,0,6]
ends =[]
for line in input[:-1].split("\n"):
#	turn the moves in the stratagy guide into numbers and then take their difference
	t = moves[line[0]]-moves[line[2]]
#	[outcome score, score for my move]
	e = [outcome[t],moves[line[2]]]
	ends.append(e)

#doing all the summation
print(sum([sum(i) for i in ends]))

#one way to calculate my move is to use the guid as numbers and sum them for keys of the outcomes..
#with the numbers i chose you need to re-order outcomes.. 
moves, outcome = dict(zip(list("ABCXYZ"),[1,2,3,-1,0,1])), [3,6,0]
ends =[]
for line in input[:-1].split("\n"):
#	turn the moves in the stratagy guide into numbers and then add them
	t = (moves[line[0]]+moves[line[2]])%3
#	[outcome score, score for my move]
	e = [outcome[moves[line[2]]],t if t else 3]
	ends.append(e)

#doing all the summation
print(sum([sum(i) for i in ends]))
