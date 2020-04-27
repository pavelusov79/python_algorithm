#2. Отсортируйте по возрастанию методом слияния одномерный
# вещественный массив, заданный случайными числами на промежутке
# [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

lst = [round(random.uniform(0, 50), 2) for i in range(10)]
print('исходный массив: ', lst)

def merge(first, second):
    sorted_lst = []
    first_ind, second_ind = 0, 0
    for _ in range(len(first) + len(second)):
        if first_ind < len(first) and second_ind < len(second):
            if first[first_ind] <= second[second_ind]:
                sorted_lst.append(first[first_ind])
                first_ind += 1
            else:
                sorted_lst.append(second[second_ind])
                second_ind += 1
        elif first_ind == len(first):
            sorted_lst.append(second[second_ind])
            second_ind += 1
        elif second_ind == len(second):
            sorted_lst.append(first[first_ind])
            first_ind += 1
    return sorted_lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    first = merge_sort(arr[: len(arr)//2])
    second = merge_sort(arr[len(arr)//2:])
    return merge(first, second)

print('отсортированный массив: ', merge_sort(lst))