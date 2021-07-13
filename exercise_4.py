#Скопировала, так как не знала как решать
num = int(input('Введите любое число - '))
max = num % 10
n = num

while n > 0:
    digit = n % 10
    if digit > max:
        max = digit

    if digit == 9:
        break

    n = n // 10
    print(n)
print(f'Наибольшая цифра в числе {num} - {max}')




