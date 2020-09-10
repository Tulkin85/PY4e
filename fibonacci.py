def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1)+fibonacci(n-2)

inp = int(input('Please input number: '))
print(fibonacci(inp))
