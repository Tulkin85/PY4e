def chop(t):
    del t[0]
    del t[-1]
a = [1, 3, 4, 5]
mylist = chop(a)
print(a)
print(mylist)

def middle(t):
    return t[1:-1]

b = [10, 30, 40, 50,70,90]
mylist1 = middle(b)
print(b)
print(mylist1)
