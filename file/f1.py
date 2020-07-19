fhand  = open('something.txt')
print(fhand)

for l in fhand:
    print(l)
    
    
inp = fhand.read()
print(inp)
print(len(inp))
