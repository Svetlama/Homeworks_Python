i = float(input("Выручка: "))
c = float(input("Издержки: "))

if i > c:
    print(f"Фирма работает с прибылью.Рентабельность выручки составила {int(i/c)}")
    n = int(input("Численность сотрудников предприятия: "))
    print (f"Прибыль фирмы в расчёте на одного сотрудника {int(i-c)/n}")
elif i == c:
    print(f"Фирма работает в ноль.")
else:
    print("Фирма работает в убыток.")

