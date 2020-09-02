largest = None

for i in [3,13,16,3,30]:
    if largest is None or i>largest:
        largest = i
    print('Loop: ', i, largest)
