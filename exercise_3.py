n = input('Введите любое положительное целое число n - ')
if int(n)>0:
    # print('n = ', n)
    # m = int(n + n)
    # print('nn = ', m)
    # l = int(n + n + n)
    # print('nnn = ', l)
    # n = int(n)
    # p = n + m + l
    # print('Результат выражения n + nn + nnn = ', p)
    print(f'{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}')
else:
    print('Введенное число неверно')


