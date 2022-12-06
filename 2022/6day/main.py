#example input used to test basics
inputs =["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
	"bvwbjplbgvbhsrlpgdmjqwftvncz",
	"nppdvjthqldpwncqszvftbrmjlhg",
	"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
	"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]

with open("part1.input") as i:
        inputs.append(i.read()[:-1])

for input in inputs:

	print("part1")
	offset =0
	while offset <= (len(input)-4):
		sstart,send = [offset,offset+4]
		a,b,c,d = input[sstart:send]
	#	print(a,b,c,d)
		if a!= b and a!=c and a!=d:
			if b!=c and b!=d:
				if c!=d:
					break
				else:
					offset +=3
					continue
				offset += 2
				continue
		offset += 1
	print(offset+4)

	print("part2")
	offset =0
	while offset <= (len(input)-14):
		sstart,send = [offset,offset+14]
		slice = input[sstart:send]
	#	print(*slice)
		dups = []
		for ind,itm in enumerate(slice):
			if slice.count(itm) > 1:
				if slice.rfind(itm) != ind:
					dups.append(ind)
		if dups:
			offset += 1 + max(dups)
		else: break
	print(offset+14)


