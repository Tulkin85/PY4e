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
        word = words[1]
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

lst = list()
for key, value in list(counts.items()):
    lst.append((value, key))

lst.sort(reverse=True)

for key, value in lst[:1]:
    print(key,value)
