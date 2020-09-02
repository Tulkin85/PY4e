fname = input('Enter the file name: ')
if fname == 'na na boo boo':
    print('NA NA BOO BOO To You - you have been punked')
    exit()

try:
    fhand = open(fname)
except:
    print('File can not be opened', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count +=1
print('There were', count, 'subject lines in', fname)
