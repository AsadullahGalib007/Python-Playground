import re
x = 'My favourite 2 numbers are 21 and 92'



print('Using [0-9]+\t: ',re.findall('[0-9]+',x))
print('Using [0-9]\t: ',re.findall('[0-9]',x))
print('Using [AEIOU]+\t: ',re.findall('[AEIOU]+',x))