inp = input('Enter a file name: ')
fhand = open(inp)
#print(fhand)

mylist = []
for line in fhand:
    words = line.split()
    #print(words)
    for word in words:
        if word in mylist:
            continue
        mylist.append(word)

print(sorted(mylist))
