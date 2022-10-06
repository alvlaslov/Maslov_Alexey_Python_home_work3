# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Input a number: '))
s = ''
n = number
while n:
    s = str(n % 2) + s
    n //= 2
print(f'The number "{number}" in the binary system of calculus = {s}')