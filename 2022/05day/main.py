#example input used to test basics
input =	"""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

with open("part1.input") as i:
        input=i.read()[:-1]

lines = [line for line in input.splitlines()]

#find the bottom of the crate stacks
bottom=0
for index,line in enumerate(lines):
	if line[1] in "1":
		bottom = index
		break

#turn stacks into a list of list and then "turn it sideways" with the "bottom" at the left
#doesn't really make a difference that the bottom is now at the left, brain just likes thinking about it like this
stacks =[[]] + [list(stack[::-1]) for stack in zip(*[[crate for crate in line[1::4]] for line in lines[:bottom]])]
instructions = [line.split(" ") for line in lines[bottom+2:]]

#removes the whitespace in the stacks.. this does make it easier to deal with
for x,stack in enumerate(stacks):
	for y,crate in enumerate(stack):
		if crate ==" ":
			del stacks[x][y:]
			break

print(stacks)
#print(instructions)
for inst in instructions:
	crates,froms,tos = [int(i) for i in[inst[1],inst[3],inst[5]]]
# line does part one
#	for i in range(0,crates): stacks[tos].append(stacks[froms].pop())

# lines for part 2
	lens = len(stacks[froms])
	for crate in stacks[froms][lens-crates:]:
		stacks[tos].append(crate)
	del stacks[froms][lens-crates:]


print(stacks)
print(*[ i.pop() if i else "" for i in stacks],sep="")
