a = list(input('Введите через пробел элементы списка ').split(' '))
for b, element in enumerate(a, 1):
    if len(element) > 10:
        element = element[0:10]
    print(f"{b}. {element}")
