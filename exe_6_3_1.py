def count(my_string, my_letter):
    my_count = 0
    for i in my_string:
        if i == my_letter:
            my_count = my_count + 1
    print(my_count)

count('Aziz','z')
