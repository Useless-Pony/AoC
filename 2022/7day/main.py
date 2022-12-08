#example input used to test basics
inputs =["""
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""[1:]]

with open("part1.input") as i:
        inputs.append(i.read()[:-1])


for input in inputs:
	dirs={"/":0}
	files={}
	pwd="/"
	for line in input.splitlines():
		strm = line.split(" ")
		if line[0] =="$":
			#cmd
			if strm[1] == "cd":
				if strm[2] == "/": pwd = "/"
				elif strm[2] == "..": pwd = pwd[:pwd[:-1].rfind("/")] + "/"
				else: pwd = pwd + strm[2] + "/"
			elif strm[1] == "ls": pass
		else:
			#data
			if strm[0] == "dir":
				dirs.setdefault(pwd + strm[1] + "/")
			else:
				files.setdefault(pwd + strm[1], int(strm[0]))
	for dir in dirs:
		total=0
		for file in files:
			if dir in file:
				total += files[file]
		dirs[dir]=total

	print("##part1")

	print(sum([size if size <= 100000 else 0 for size in dirs.values()]))

	print("##part2")

	total_sp, update = 70000000, 30000000
	max_usable = total_sp - update
	excess = dirs["/"] - max_usable
	print(excess)
	print(min([size if size > excess else int("9"*9*9) for size in dirs.values()]))

print("done")
