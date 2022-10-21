def calculate(a, b, op):
    result = 0.0
    match op:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '/':
            result = a / b
        case '*':
            result = a * b
        case 'mod':
            result = a % b
        case 'pow':
            result = a ** b
        case 'div':
            result = a // b
        case _:
            return False
    return result


try:
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    op = input('Введите операцию: ')
    if b == 0 and (op == '/' or op == 'mod' or op == 'div'):
        print('Деление на 0!')
    else:
        result = calculate(a, b, op)
        print(f'a={a}, b={b}, op="{op}" -> '
              f'{"Непонятная операция" if result is False else result}')
except ValueError:
    print('Вы ввели не число.')