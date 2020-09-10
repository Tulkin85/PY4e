def check(a,b,c,n):
    if n>2:
        if a**n + b**n == c**n:
            print('Holy smokes, Fermat was wrong!')
        else:
            print('No, that does not work')

a = input('Please input a\n')
b = input('Please input b\n')
c = input('Please input c\n')
n = input('Please input n\n')

check(int(a), int(b),int(c), int(n))
