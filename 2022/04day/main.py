#example input used to test basics
input =	"""2-4,6-8
	2-3,4-5
	5-7,7-9
	2-8,3-7
	6-6,4-6
	2-6,4-8	"""

with open("part1.input") as i:
        input=i.read()[:-1]

count =0
for line in input.splitlines():
	ranges = [[int(i) for i in range.split("-")]for range in line.split(",")]
	for i in [0,1]:
		if ranges[i][0] <= ranges[abs(i-1)][0] and ranges[i][1] >= ranges[abs(i-1)][1]:
			count +=1
			break

print(count)

count =0
for line in input.splitlines():
	ranges = [[int(i) for i in range.split("-")]for range in line.split(",")]
	for i in [0,1]:
		if ranges[i][0] <= ranges[abs(i-1)][1] and ranges[i][1] >= ranges[abs(i-1)][0]:
			count +=1
			break

print(count)
