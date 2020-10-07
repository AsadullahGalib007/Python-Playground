name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = {}
for line in handle:
	if line.startswith('From') and not line.startswith('From:') and ':' in line:
		words = line.split()
		word = words[5]
		word = word.split(":")
		v = word[0]
		counts[v] = counts.get(v,0)+1


counts = sorted(counts.items())
for v,k in counts:
	print(v,k)

