isLoop = True
summa = 0
while isLoop:
    userinput = input('Введите цифры через пробел (перед/после ввода пробел не ставить) ').split(' ')
    a = list()
    for n in userinput:
        try:
            a.append(int(n))
        except:
            ValueError
            isLoop = False
            break
    summa = sum(a)+summa
    print(summa)