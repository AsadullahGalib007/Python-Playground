fname = input("Enter a filename to create a file: ")


if ".txt" not in fname:
	fname = fname + ".txt"

fout = open(fname,'w')
_str = input("Enter some data: ")

while _str != 'done':
	_str = input()
	fout.write(_str)

fout.close()

fopen = open(fname,'r')

for line in fopen:
	print(line)