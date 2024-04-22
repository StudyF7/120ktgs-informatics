speed = int(input('Скорость интернета в кб: '))
time = int(input('Время в минутах: '))
file = speed*time
print(f'Размер файла: {file} Кб')
rubkb = int(input('Рублей за Кб: '))
if file>500:
    coast = ((file-500)*rubkb)
    print(f'Стоимость: {coast} ₽')
else:
    print('Бесплатно')