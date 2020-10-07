fhand = open('something.txt')

for l in fhand:
	if l.startswith('Hello'):
		print(l)
