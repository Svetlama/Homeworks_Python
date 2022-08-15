def my_divide():
    a = int(input('Введите число а '))
    b = int(input('Введите число b '))
    return a / b

while True:
    try:
        print(my_divide())
        break
    except ZeroDivisionError:
        print('На 0 делить нельзя')
    except ValueError:
        print('Введено некорректное значение')
