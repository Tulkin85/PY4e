file = input('Enter the file name: ')

fhand = open(file)
count = 0
count_sum = []
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        inp = float(line[line.find(':')+1:])
        count_sum.append(inp)

print('Average spam confidence', sum(count_sum)/count)
