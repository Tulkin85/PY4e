def do_twice(f, a):
    f(a)
    f(a)
#
# def print_spam(a):
#     print(a)

def print_twice(t):
    print(t)
    print(t)

do_twice(print_twice, 'spam')
