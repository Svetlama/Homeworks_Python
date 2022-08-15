print('Программа возводит x (>0) в степень -y. ')
firstInput = float(input('x = '))
secondInpur = int(input('y (со знаком "-") = '))
def my_func(x,y):
    if x < 0:
        print(ValueError('Неверные аргументы'))
    elif int(y) != float(y) or y >= 0:
        print(ValueError('Неверные аргументы'))
    else:
        return x**y
print(my_func(firstInput,secondInpur))

