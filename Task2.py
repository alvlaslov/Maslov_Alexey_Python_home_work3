# 2) Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

ls = []
ls_sum = []
ls_len = int(input('Input the length of list: '))
for i in range(ls_len):
    ls.append(int(input('Input a number: ')))
for i in range((ls_len + 1) // 2):
    ls_sum.append(ls[i] * ls[ls_len - i - 1])
print(f'{ls} => {ls_sum}')



