import re
reg_exp  = str(input('Enter a regular expression: '))
textfile = open('mbox.txt')

count = 0

for line in textfile:
    line = line.rstrip()
    if re.findall(reg_exp, line):
        count +=1

print('mbox.txt had', count, 'lines that matched', reg_exp)
