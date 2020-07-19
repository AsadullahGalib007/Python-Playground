

txt = input("Enter a string: ")
l = len(txt)


if l<2:
	print("Expected output: ")
else:
	data = txt[0] + txt[1] + txt[l-2] + txt[l-1]
	print(data)