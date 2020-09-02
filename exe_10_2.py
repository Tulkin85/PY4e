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
        word = words[5].split(':')[0]
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

lst = list()
for key, value in list(counts.items()):
    lst.append((key, value))

lst.sort()

for key, value in lst[:]:
    print(key,value)
