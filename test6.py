# # практика 1
# is_rainy = input('Дождь? ')
#
# if is_rainy == 'True':
#     heavy_rain = input('Сильный дождь? ')
#     if heavy_rain == 'True':
#         print('Надеваю дождевик')
#     else:
#         print('Беру зонт')
#     print('Иду гулять')
# elif is_rainy == 'False':
#     print('Не беру зонт')
#     print('Иду гулять')
# else:
#     print('Неверное значение')
#     print('Не иду гулять')
#
# # практика 2
# example = (2 > 3) and (2< 2) or (1 != 5) and (not (5 < 3) or (3 == 1))
#
# my_result = False and False or True and (not False or False)
# my_result = False and False or True and (True or False)
# my_result = (False and False) or (True and True)
# my_result = False or True
# my_result = True
#
# print(example)
# print(my_result)
# print(example == my_result)
#
# # практика 3
# a = int(input('Число a: '))
#
# if a > 10:
#     print('a больше 10')
# elif a < 10:
#     print('a меньше 10')
# else:
#     print('a равно 10')
#
# # практика 4
# str_1 = 'test'
# str_2 = "test"
# str_3 = '''test'''
# str_4 = """test"""
#
# print(str_1 == str_2 == str_3 == str_4)
# print(
#     (str_1 == str_2)
#     and (str_2 == str_3)
#     and (str_3 == str_4)
# )
#
# # практика 5
# for i in range(3):
#     print(i+1, "шаг цикла")
# print("Первый цикл закончился!")
#
# # практика 6
# for value in [1, 2, 3, 4, 5]:
#     print(value)
# for value in (1, 2, 3, 4, 5):
#     print(value)
# for value in {1, 2, 3, 4, 5}:
#     print(value)
#
# # практика 7
# print(range(10))
# print(list(range(10)))
#
# print(tuple(range(1, 11)))
#
# print(list(range(1, 11, 2)))
#
# print(tuple(range(10, 0, -1)))
#
# # практика 8
# for _ in range(5):
#     print("Hello World!")
#
# #
#
# numbers = [10, 20, 30, 40, 50]
#
# total = 0
#
# for i in range(len(numbers)):
#     total += numbers[i]
#
# print("Сумма чисел: ", total)
#
# # практика 9
# for pos, value in enumerate("абв", start=1):
#     print("Позиция: ", pos, "->", "Значение", value)
#
# # практика 10
# count = 0
# while count < 5:
#     print("Значение count", count)
#     count += 1
#
# # задача 1
# str_ = "Строка с цифрой 1"
#
# is_substr = "Строка" in str_ # True
# print("В строке есть слово Строка?", is_substr)
#
# # задача 2
# number = 12
#
# condition_1 = number % 2 == 0 # число кратно 2
# condition_2 = number % 3 == 0 # число кратно 3
#
# if condition_1 and condition_2:
#     print('Число кратно 2 и 3')
# else:
#     print('Число не (кратно 2 и 3)')
#
# # задача 3
# mount = 12
#
# # символ \ позволяет визуально разбить команду, для интерпретатора это одна строка
# bad_condition = \
#     mount == 12 or \
#     mount == 1 or \
#     mount == 2 # Очень плохая запись условия
#
# good_condition = mount in [12, 1, 2] # При множественном сравнении лучше использовать in
#
# if good_condition:
#     print("Зима!!!")
#
# # задача 4
# hour = 7
#
# bad_condition = (6 <= hour) and (hour < 12) # цепочки операторов всегда соединяются через AND
# good_condition = 6 <= hour < 12
#
# if good_condition:
#     print("Утро!!!")
#
# # задача 5
# list_ = [5, 6, 7, 8, 9]
#
# result = (4 in list_) and (8 in list_)
# print(result)