sec = int(input('Введите время в секундах - '))

# Способ 1
ch= sec // 3600
min = sec // 60 - ch * 60
sec = sec - ch * 3600 - min * 60
print(f'{ch:02}:{min:02}:{sec:02}')

#Способ 2
sec = int(input('Введите время в секундах - '))
ch = sec // 3600
sec = sec % 3600
min = sec // 60
sec = sec % 60
print(f'Время в часах, минутах и секундах - {ch:02}:{min:02}:{sec:02}')
