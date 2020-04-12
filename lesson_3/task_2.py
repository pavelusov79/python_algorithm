# 2. Во втором массиве сохранить индексы четных элементов первого
# массива. Например, если дан массив со значениями 8, 3, 15, 6, 4,
# 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно
# в этих позициях первого массива стоят четные числа.

import random

size = 10
min_num = 0
max_num = 100
massiv_2 = []
massiv_1 = [random.randint(min_num, max_num) for i in range(size)]
for i in range(len(massiv_1)):
    if massiv_1[i] % 2 == 0:
        massiv_2.append(i)

print('исходный massiv_1: ', massiv_1)
print('индексы четных чисел massiv_1: ', massiv_2)
