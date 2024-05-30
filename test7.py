# # 1
# for i in range(3):
#     print(i+1, "шаг цикла")
# print("Первый цикл закончился!")
#
# # 2
# for value in [1, 2, 3, 4, 5]:
#     print(value)
# for value in (1, 2, 3, 4, 5):
#     print(value)
# for value in {1, 2, 3, 4, 5}:
#     print(value)
#
# # 3
# print(range(10))
# print(list(range(10)))
#
# print(tuple(range(1, 11)))
#
# print(list(range(1, 11, 2)))
#
# print(tuple(range(10, 0, -1)))
#
# # 4
# for _ in range(5):
#     print("Hello World!")
#
# # 5
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
# # практика 6
# for pos, value in enumerate("абв", start=1):
#     print("Позиция: ", pos, "->", "Значение", value)
#
# # практика 7
# count = 0
# while count < 5:
#     print("Значение count", count)
#     count += 1