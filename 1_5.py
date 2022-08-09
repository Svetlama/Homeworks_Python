p = float(input("Выручка: "))
c = float(input("Издержки: "))
if p > c:
    print("Фирма работает с прибылью.")
if p == c:
    print("Фирма работает в ноль.")
else:
    print("Фирма работает в убыток.")
