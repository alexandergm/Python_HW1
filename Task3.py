def get_quarter(x, y):
    if x > 0:
        if y > 0:
            return 1
        return 4
    if y > 0:
        return 2
    return 3


try:
    x = float(input('Введите координату x:'))
    if x == 0:
        print('x не может быть равен 0 по условию задачи.')
    else:
        y = float(input('Введите координату y:'))
        if x == 0:
            print('y не может быть равен 0 по условию задачи.')
        else:
            print(f'x={x}; y={y} -> {get_quarter(x, y)}')
except ValueError:
    print('Вы ввели не число.')
