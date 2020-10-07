fhand = open('something.txt')


	
	
for line in fhand:
	line = line.rstrip()
	if 'name' in line:
		print(line)
