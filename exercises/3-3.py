


r = float(input("Enter a Score: "))

if r<0.0 or r>1.0:
	print("Invalid\n")
		
		
else:
	if r<0.6:
		print("F")
	elif r>=0.6 and r<0.7:
		print("D")
	elif r>=0.7 and r<0.8:
		print("C")
	elif r>=0.8 and r<0.9:
		print("B")
	elif r>=0.9:
		print("A")
