fhand = open('words.txt')
count = 0
dictionary_words = {}
for line in fhand:
    words = line.split()
    for word in words:
        count = count + 1
        if word in dictionary_words:
            continue
        dictionary_words[word] = count

print(dictionary_words)

if 'Python' in dictionary_words:
    print('True')
else:
    print('False')
