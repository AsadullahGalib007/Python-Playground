


txt = 'google.com'

for l in txt:
	count = 0
	for i in txt:
		if l==i:
			count = count+1
	print(l, count)