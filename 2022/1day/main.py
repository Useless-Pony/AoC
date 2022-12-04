#! bin/python

#example input used to test basics
input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

with open("part1.input") as i:
        input=i.read()

# [[[calories, ...], <reserved for sum>], ...]
def structurize(serialdata):
	data=[]
	for group in serialdata[:-1].split("\n\n"):
		data.append([[int(line) for line in group.split("\n")]])
	return(data)

s=structurize(input)
# add the sums into the structurized data
for index, item in enumerate(s):
        s[index].append(sum(item[0]))

#find the top #a of the structurized data
def top(number):
        output=[]
        for _ in range(number):
                tmp=["",0]
                for index, item in enumerate(s):
                        if item[1] > tmp[1] :
                                tmp = [index, item[1]]
                if tmp[0]: output.append(s.pop(tmp[0]))
        return output

#print top 3 so part1 can still be done without duplicat code.
top = top(3)
print(top)

#sum the top3 and print
a=0
for i in top:
        a += i[1]
print(a)
