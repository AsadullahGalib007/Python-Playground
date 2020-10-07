import re
fname =  input('Enter File name: ')

if len(fname) < 1:
	fname = 'regex_sum_815752.txt'
fhand = open(fname)


sum = 0
for line in fhand:
	line = line.rstrip()
	y = re.findall('[0-9]+',line)
	if len(y) > 0:
		for i in y:
			i = int(i)
			sum = sum + i

print(sum)