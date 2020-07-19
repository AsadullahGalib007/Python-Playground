data = input('Enter a string: ')

def modify(txt):
	pos = txt.find('ing')

	if pos > 0:
		txt = txt + 'ly'
	else:
		txt = txt + 'ing'
	return txt


print(modify(data))