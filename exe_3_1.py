xh = input('Enter Hours: ')
xr = input('Enter Rate: ')
try:
    if float(xh)>40:
        xp = float(xh) * (float(xr)+0.5)
    else:
        xp = float(xh) * float(xr)
        print('Pay:', xp)    
except:
    print('Error, please enter numeric inpui')
