fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File can not be opened', fhand)
    exit()

counts = {}

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        atops = words[1].find('@')
        domain = words[1][atops+1:]
        if domain not in counts:
            counts[domain] = 1
        else:
            counts[domain] += 1

print(counts)
