# 9.  Среди натуральных чисел, которые были введены, найти наибольшее
# по сумме цифр. Вывести на экран это число и сумму его цифр.

n = input('Введите положительные натуральные числа через пробел: ').split()
n = list(map(int, n))
is_max = 0
max_dig = n[0]
for el in n:
    d = sum(map(int, str(el)))
    if d > is_max:
        is_max = d
        max_dig = el
print(f'наибольшее число по сумме цифр: {max_dig}, сумма цифр числа: {is_max}')