# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.

a = input('Введите первое число: ')
b = input('Введите второе число: ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите первое число: ')

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Неправильно ввели!')
        b = input('Введите первое число: ')

if (a + b) % 5 == 0:
    sum = a + b
    sum += 1
    print(f'Сумма введеных чисел кратна 5 результат: {sum}')
else:
    sum = a + b
    sum -= 2
    print(f'Сумма введеных чисел не кратна 5 результат: {sum}')
