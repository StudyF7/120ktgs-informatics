# # 1
# speed = int(input('Скорость интернета в кб: '))
# time = int(input('Время в минутах: '))
# file = speed*time
# print(f'Размер файла: {file} Кб')
# rubkb = int(input('Рублей за Кб: '))
# if file>500:
#     coast = ((file-500)*rubkb)
#     print(f'Стоимость: {coast} ₽')
# else:
#     print('Бесплатно')
#
# # 2
# import math
#
# r_circle = int(input('Задайте радиус круга: '))
# squareside = int(input('Задайте сторону квадрата: '))
#
# s_circle = "{:.2f}".format(math.pi * r_circle**2)
# lenght_circle = "{:.2f}".format(2 * math.pi * r_circle)
# p_square = 4 * squareside
# s_square = squareside**2
#
# print(f'Площадь круга {s_circle}')
# print(f'Длинна круга {lenght_circle}')
# print(f'Периметр квадрата  {p_square}')
# print(f'Площадь квадрата {s_square}')
#
# # 3
# floppy = 1,44 #Mb
# pages = 100
# lines = 50
# sym = 25
# onesym = 4 #Byte
# 4*25*50*100
# books = int(1.44/(4*25*50*100/1024/1024))
#
# print(f"{books} book")
#
# # 4
# str_numbers = '0'*20 + '1'*50 + '2'*30
# print(str_numbers)