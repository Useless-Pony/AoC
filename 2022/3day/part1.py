#example input used to test basics
input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

with open("part1.input") as i:
        input=i.read()

alp="abcdefghijklmnopqrstuvwxyz"
alp=alp+alp.upper()

#something = 0
#for line in input[:-1].splitlines():
#	n=len(line)
#	thing = [line[:n//2],line[n//2:]]
#	a=0
#	for i in thing[0]:
#		if i in thing[1]:
#			a=alp.find(i)+1
#	something+=a
#print(something)


lines= [line for line in input[:-1].splitlines()]
items={}
q=0
for n in range(len(lines[::-1])):
	if n%3: continue
	for i in lines[n]:
		if (i in lines[n+1]) and (i in lines[n+2]):
			pri = alp.find(i)+1
			items.update({pri:i})
			q+= pri
			break

print(q)
