def is_weekend(n):
    return n == 6 or n == 7


try:
    num = int(input('Введите целое число: '))
    if num > 7 or num < 1:
        print(f'Нет дня недели с номером {num}')
    else:
        print(f'{num} -> {"Да" if is_weekend(num) else "Нет"}')
except ValueError:
    print('Вы ввели не целое число.')
    