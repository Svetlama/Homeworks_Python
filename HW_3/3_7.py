a = input('Введите слова через пробел ').split(' ')
def int_func(word):
    return word.title()
print(' '.join(list(map(int_func, a))))

