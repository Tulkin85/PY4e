fruit = 'banana'
index = 0
for i in range(1,len(fruit)+1):
    print(fruit[-i])

print('#####')

ind = len(fruit)-1
while ind >=0:
    letter = fruit[ind]
    print(letter)
    ind -= 1
