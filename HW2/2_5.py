my_list = [7, 5, 3, 3, 2]
print(str(my_list))
a = int(input("Введите отметку "))
while True:
    if a in my_list:
        i = my_list.index(a)
        my_list.insert(i, a)
        print(my_list)
    else:
        my_list.append(a)
        my_list.sort(reverse=True)
        print(my_list)
    a = int(input("Введите следующую отметку "))