# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

ls = []
len_ls = int(input('Input the length of the list: '))
for i in range(len_ls):
    ls.append(int(input('Input the number: ')))
print(ls)
sum = 0
for i in range(len_ls):
    if i % 2 != 0:
        sum += ls[i]
print(sum)