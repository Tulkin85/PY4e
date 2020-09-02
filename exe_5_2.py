count1 = []
user = None
while user != 'done':
    user = input('Enter a number: ')
    try:
        user = float(user)
        count1.append(user)
    except:
        print('Invalid Input')

print('Maximum:', max(count1))
print('Minimum: ', min(count1))
