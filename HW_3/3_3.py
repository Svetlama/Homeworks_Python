firstInput = int(input('x =' ))
secondInput = int(input('y =' ))
thirdInput = int(input('z = '))
def my_func(x,y,z):
    a = [x,y,z]
    minimum = min(a)
    a.remove(minimum)
    return sum(a)
print(my_func(firstInput,secondInput,thirdInput))
