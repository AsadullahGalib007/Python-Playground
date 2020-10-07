_str = 'But soft what light through yonder window breaks It is the east and Juliet is the sun Arise fair sun and kill the envious moon Who is already sick and pale with grief'
lst = []
dct = {}
lst = _str.split()
lst.sort()
for l in lst:
	dct[l] = dct.get(l,0) + 1

print(lst)
print(dct)


word = 'brontosaurus'
lst2 = []
for l in word:
	lst2.append(l)
lst2.sort()
d = dict()
for c in lst2:
	d[c] = d.get(c, 0) + 1

print(d)