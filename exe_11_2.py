
import re
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File can not be opened', fhand)
    exit()

counts = 0
lst = []

for line in fhand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9.]+)',line)
    for val in x:
        val = float(val)
        lst.append(val)

print(sum(lst)/len(lst))
