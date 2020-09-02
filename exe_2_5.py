cel_temp = input('Please enter temp: ')

try:
    far_temp = float(cel_temp)*(9/5) + 32
    print('Temp in far', far_temp)
except:
    print('Please enter a number')
