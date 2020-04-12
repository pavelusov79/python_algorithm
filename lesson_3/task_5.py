# 5.  В массиве найти максимальный отрицательный элемент. Вывести на
# экран его значение и позицию (индекс) в массиве.
import random

size = 10
max_num = 50
min_num = -50
lst = [random.randint(min_num, max_num) for i in range(size)]
print('массив:', lst)
lst_minus = []
for i in range(len(lst)):
    if lst[i] < 0:
        lst_minus.append(lst[i])
if len(lst_minus) != 0:
    min_ = lst_minus[0]
    for j in range(len(lst_minus)):
        if lst_minus[j] > min_:
            min_ = lst_minus[j]
    print('максимальное отрицательное число: ', min_)
    print('индекс макс.-отриц. числа:', lst.index(min_))
else:
    print('в массиве нет отрицательных чисел')
