arr = []

while True:
	num = input("Enter a value: ")
	if num == 'done':
		break

	try:
		num = int(num)	
	except:
		print('Invalid input')
		continue

	arr.append(num)


print('Maximum is',max(arr))
print('Minimum is',min(arr))