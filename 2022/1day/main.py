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

def structurize(n):
	a=[]
	for i in n[:-1].split("\n\n"):
		a.append([[int(q) for q in i.split("\n")]])
	return(a)

s=structurize(input)
#print(s)

for n,i in enumerate(s):
        s[n].append(sum(i[0]))

#print(s)

def top(a):
        o=[]
        for e in range(a):
                q=["",0]
                for n,i in enumerate(s):
                        if i[1] > q[1] :
                                q = [n,i[1]]
                if q[0]: o.append(s.pop(q[0]))
        return o

top = top(3)

print(top)

a=0
for i in top:
        a += i[1]
print(a)
