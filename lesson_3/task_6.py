# 6. В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами. Сами минимальный и
# максимальный элементы в сумму не включать.

import random

size = 10
min_num = -50
max_num = 50
lst = [random.randint(min_num, max_num) for i in range(size)]
print('исходный массив: ', lst)
max_n = lst[0]
min_n = lst[0]
sum_ = 0
for i in range(len(lst)):
    if lst[i] > max_n:
        max_n = lst[i]
    elif lst[i] < min_n:
        min_n = lst[i]
m = lst.index(max_n)
n = lst.index(min_n)
if m > n:
    lst_1 = lst[n + 1:m]
else:
    lst_1 = lst[m + 1:n]
for i in range(len(lst_1)):
    sum_ += lst_1[i]
if abs(m - n) > 1:
    print('срез между макс и мин:', lst_1)
    print(f'сумма между макс и мин элементами массива: {sum_}')
else:
    print('между макс. и мин. элементами нет диапазона')
