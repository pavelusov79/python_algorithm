#3. Массив размером 2m + 1, где m — натуральное число, заполнен
# случайным образом. Найдите в массиве медиану. Медианой называется
# элемент ряда, делящий его на две равные части: в одной находятся
# элементы, которые не меньше медианы, в другой — не больше медианы.
import random
m = random.randint(1, 6)
lst = [random.randint(1, 50) for m in range(2 * m + 1)]
print('исходный массив: ', lst)
med = sum(lst) / len(lst)
left = []
right = []
for i in lst:
    if i < med:
        left.append(i)
    else:
        right.append(i)
max_left = left[-1]
min_right = right[0]
for i in range(len(left)):
    if left[i] > max_left:
        left[i], left[-1] = left[-1], left[i]
for i in range(len(right)):
    if right[i] < min_right:
        right[i], right[0] = right[0], right[i]
new_lst = left + right
print('new_lst: ', new_lst)
print('медиана: ', new_lst[len(new_lst) // 2])


