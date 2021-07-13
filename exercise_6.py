a = float(input('Введите результат 1ого дня ( в км ) - '))
b = float(input('Результат не меньше ( в км ) - '))
day = 1

while a < b:
    print(f'{day} день - {round(a, 2)} км')
    day =  day + 1
    a = a + (a * 0.1)

a >= b
day =  day + 1
a = a + (a * 0.1)
print(f'{day} день - {round(a, 2)} км')
print('Задача решена')
