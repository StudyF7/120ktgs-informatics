import math

r_circle = int(input('Задайте радиус круга: '))
squareside = int(input('Задайте сторону квадрата: '))

s_circle = "{:.2f}".format(math.pi * r_circle**2)
lenght_circle = "{:.2f}".format(2 * math.pi * r_circle)
p_square = 4 * squareside
s_square = squareside**2

print(f'Площадь круга {s_circle}')
print(f'Длинна круга {lenght_circle}')
print(f'Периметр квадрата  {p_square}')
print(f'Площадь квадрата {s_square}')
