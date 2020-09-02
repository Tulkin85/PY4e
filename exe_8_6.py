my_list = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    my_list.append(inp)

print('Maximum', max(my_list))
print('Minimum', min(my_list))
    
