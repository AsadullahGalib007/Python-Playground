msg1 = "Enter a year: "
msg2 = "is not a leapyear."
msg3 = "is a leapyear."


while(1):
	y = int(input(msg1))

	if y%4 == 0:
		if y%100 == 0:
			if y%400 == 0:
				print(y,msg3)
			else:
				print(y,msg2)
		else:
			print(y,msg3)
	else:
		print(y,msg2)

