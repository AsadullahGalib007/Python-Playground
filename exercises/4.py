


def replace_occurances(_str):
	ch = _str[0]
	data = _str.replace(ch,'$')
	_str = _str[0] + data[1:]
	return _str


txt = input("Enter data: ")
print(replace_occurances(txt))