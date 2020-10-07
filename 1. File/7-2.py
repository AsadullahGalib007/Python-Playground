

fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
    	count = count+1
    	_str, _no = line.split(' ')
    	_no = float(_no)
    	total = total + _no

avg = total/count
print('Average spam confidence:',avg)

    