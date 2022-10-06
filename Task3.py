#  Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#Method1 - целые числа исключаются из расчета

ls = []
ls_len = int(input('Input the length of list: '))
for i in range(ls_len):
    ls.append(float(input('Input a number: ')))
max = ls[0] % 1
for i in range(ls_len):
    if ls[i] % 1 != 0 and ls[i] % 1 > max:
        max = ls[i] % 1
min = max
for i in range(ls_len):
    if ls[i] % 1 != 0 and ls[i] % 1 < min:
        min = ls[i] % 1
print(max, min)
print(f'The difference between the maximum and minimum values of the fractional part of the elements = {round((max - min), 2)}')



# Method2 - у целого числа дробная часть считается равной ".0"
#*Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.2

# ls = []
# ls_len = int(input('Input the length of list: '))
# for i in range(ls_len):
#     ls.append(float(input('Input a number: ')))
# max = ls[0] % 1
# min = ls[0] % 1
# for i in range(ls_len):
#     if ls[i] % 1 != 0 and ls[i] % 1 > max:
#         max = ls[i] % 1
#     elif ls[i] % 1 != 0 and ls[i] % 1 < min:
#         min = ls[i] % 1
#     elif ls[i] % 1 == 0:
#         min = 0
# print(f'The difference between the maximum and minimum values of the fractional part of the elements = {round((max - min), 2)}')
