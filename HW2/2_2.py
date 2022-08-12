a = list(input('Введите через запятую элементы списка ').split(','))
result = [None] * len(a)
i = 0

while i < len(a):
    if i % 2 == 0:

        if i+1 == len(a):
            result[i] = a[i]
        else:
            result[i] = a[i + 1]

    else:
        result[i] = a[i - 1]
    i += 1

print(result)

