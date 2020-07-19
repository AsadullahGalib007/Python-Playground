fname = input('Enter file name: ')
handle = open(fname)



dct = {}
for line in handle:
	line = line.strip()
	if line.startswith('From') and not line.startswith('From:'):
		words = line.split()
		key = words[1]
		dct[key] = dct.get(key, 0) + 1
# print(dct)


bigCount = None
bigWord = None
for word, count in dct.items():
	if bigCount is None or count > bigCount:
		bigWord = word
		bigCount = count

print(bigWord, bigCount)