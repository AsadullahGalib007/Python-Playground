import re
fname = input('Enter file name: ')


lst = []
_sum = 0
count = 0
if len(fname) < 1:
	fname = 'mbox-short.txt'
fhand = open(fname)

for line in fhand:
	line = line.rstrip()
	y = re.findall('^N.* R.*: [0-9]+', line)
	if len(y) != 0:
		x = y[0].split()
		x = int(x[2])
		_sum = _sum+x
		count = count+1
print(int(_sum/count))

