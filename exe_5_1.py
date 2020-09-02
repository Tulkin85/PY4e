count1 = []
user = None
while user != 'done':
    user = input('Enter a number: ')
    try:
        user = float(user)
        count1.append(user)
    except:
        print('Invalid Input')

print('Total:', sum(count1))
print('Count: ', len(count1))
print('Average: ', sum(count1)/len(count1))
