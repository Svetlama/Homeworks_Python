a = float(input("x="))
b = float(input("y="))
c = input("Введите оператор (+,-,*,/) ")
if b == 0:
    print ('на 0 делить нельзя')
elif c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/':
    print (a/b)
else:
    print ('неизвестная операция')
