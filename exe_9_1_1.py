count = 0
my_dict = {}

fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count = count + 1
        if word in my_dict:
            continue
        my_dict[word] = count

print(my_dict)
