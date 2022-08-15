def print_person(name = input('Имя: '),
                 surname = input('Фамилия: '),
                 year = input('Год рождения: '),
                 city = input('Место проживания: '),
                 email = input('Email: '),
                 tel = input('Телефон: ')):
    #return locals() - как второй вариант вывода данных о пользователе одной строкой
    return name + ' ' + surname + ' ' + year + ' ' + city + ' '+ email + ' '+ tel
print(print_person())

