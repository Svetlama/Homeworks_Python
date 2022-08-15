print('Программа возводит x (>0) в степень -y. ')
firstInput = float(input('x = '))
secondInput = int(input('y (со знаком "-") = '))
def my_func(x,y):
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1/result
print(my_func(firstInput,secondInput))