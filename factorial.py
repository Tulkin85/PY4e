def factorial(n):
    if not isinstance(n, int):
        print('Has to be integer')
        return None

    elif n < 0:
        print('Has to be positive integer')
        return None

    elif  n == 0 :
        return 1

    else:
        return n * factorial(n-1)

inp = int(input('Please input number: '))

print(factorial(inp))
