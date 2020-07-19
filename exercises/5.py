

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

def modify():
	global str1
	global str2
	ch1 = str1[len(str1)-1]
	ch2 = str2[len(str2)-1]
	str1 = str1[0:len(str1)-1] + ch2
	str2 = str2[0:len(str2)-1] + ch1

modify()

print(str1, str2)