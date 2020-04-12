# 3.  В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random

size = 10
min_num = -50
max_num = 50
lst = [random.randint(min_num, max_num) for i in range(size)]
print('Исходный массив: ', lst)
max_n = lst[0]
min_n = lst[0]
for i in range(len(lst)):
    if lst[i] > max_n:
        max_n = lst[i]
    elif lst[i] < min_n:
        min_n = lst[i]
max_index = lst.index(max_n)
min_index = lst.index(min_n)
lst[max_index], lst[min_index] = lst[min_index], lst[max_index]

print('максимальное число: ', max_n)
print('минимальное число: ', min_n)
print('конечный массив: ', lst)
