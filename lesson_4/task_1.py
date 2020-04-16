# 5.  В массиве найти максимальный отрицательный элемент. Вывести на
# экран его значение и позицию (индекс) в массиве.

import random
import timeit
import cProfile

def variant_1(size):
    max_num = 1000
    min_num = -1000
    lst = [random.randint(min_num, max_num) for i in range(size)]
    lst_minus = []
    for i in range(len(lst)):
        if lst[i] < 0:
            lst_minus.append(lst[i])
    if len(lst_minus) != 0:
        min_ = lst_minus[0]
        for j in range(len(lst_minus)):
            if lst_minus[j] > min_:
                min_ = lst_minus[j]
        return f'массив: {lst}\n' \
               f'максимальное отрицательное число: {min_}\n' \
               f'индекс макс. отриц. числа: {lst.index(min_)}'
    else:
        return f'массив: {lst}\n' \
               f'в массиве нет отрицательных чисел'


# print(timeit.timeit('variant_1(10)', number = 100, globals=globals())) #0.1298285339726135
# print(timeit.timeit('variant_1(100)', number = 100, globals=globals())) #0.6271017019171268
# print(timeit.timeit('variant_1(250)', number = 100, globals=globals())) #0.7276469960343093
# print(timeit.timeit('variant_1(500)', number = 100, globals=globals())) #0.7905825800262392
# print(timeit.timeit('variant_1(1000)', number = 100, globals=globals())) #1.3824008830124512
# print(timeit.timeit('variant_1(2000)', number = 100, globals=globals())) #2.813973610987887
# print(timeit.timeit('variant_1(4000)', number = 100, globals=globals())) #5.376445924979635
# print(timeit.timeit('variant_1(8000)', number = 100, globals=globals())) #11.166260426980443
# print(timeit.timeit('variant_1(50000)', number = 100, globals=globals())) #61.63213824699051
# print(timeit.timeit('variant_1(75000)', number = 100, globals=globals())) #87.539301746001

# cProfile.run('variant_1(10)') #1    0.000    0.000    0.001    0.001 task_1.py:8(variant_1)
# cProfile.run('variant_1(100)') #1    0.001    0.001    0.013    0.013 task_1.py:8(variant_1)
# cProfile.run('variant_1(250)') #1    0.006    0.006    0.022    0.022 task_1.py:8(variant_1)
# cProfile.run('variant_1(500)') # 1    0.003    0.003    0.039    0.039 task_1.py:8(variant_1)
# cProfile.run('variant_1(1000)') #1    0.004    0.004    0.112    0.112 task_1.py:8(variant_1)
# cProfile.run('variant_1(2000)') #1    0.013    0.013    0.205    0.205 task_1.py:8(variant_1)
# cProfile.run('variant_1(4000)') #1    0.016    0.016    0.342    0.342 task_1.py:8(variant_1)
# cProfile.run('variant_1(8000)') #1    0.036    0.036    0.635    0.635 task_1.py:8(variant_1)
# cProfile.run('variant_1(50000)') #1    0.117    0.117    2.119    2.119 task_1.py:8(variant_1)

print('-' * 50)
# Вариант 2
def variant_2(size):
    max_num = 1000
    min_num = -1000
    lst = [random.randint(min_num, max_num) for i in range(size)]
    min_item = min_num
    for item in lst:
        if item < 0:
            if item > min_item:
                min_item = item

    if min_item in lst and min_item < 0:
        return f'массив: {lst}\n' \
               f'макс. отриц число: {min_item}\n' \
               f'индескс макс. отриц. числа: {lst.index(min_item)}'
    else:
        return f'массив: {lst}\n' \
               f'в массиве нет отицательных чисел'


# print(timeit.timeit('variant_2(10)', number = 100, globals=globals())) #0.02433117595501244
# print(timeit.timeit('variant_2(100)', number = 100, globals=globals())) #0.19345950102433562
# print(timeit.timeit('variant_2(250)', number = 100, globals=globals())) #0.3344837340991944
# print(timeit.timeit('variant_2(500)', number = 100, globals=globals())) #0.6543424839619547
# print(timeit.timeit('variant_2(1000)', number = 100, globals=globals())) #1.5765699869953096
# print(timeit.timeit('variant_2(2000)', number = 100, globals=globals())) #2.6689620329998434
# print(timeit.timeit('variant_2(4000)', number = 100, globals=globals())) #5.207439690013416
# print(timeit.timeit('variant_2(8000)', number = 100, globals=globals())) #10.367436714936048
# print(timeit.timeit('variant_2(50000)', number = 100, globals=globals())) #57.44739039200067
# print(timeit.timeit('variant_2(75000)', number = 100, globals=globals())) #83.57862263500283

# cProfile.run('variant_2(10)') #1    0.000    0.000    0.001    0.001 task_1.py:49(variant_2)
# cProfile.run('variant_2(100)') #1    0.000    0.000    0.006    0.006 task_1.py:49(variant_2)
# cProfile.run('variant_2(250)') #1    0.001    0.001    0.021    0.021 task_1.py:49(variant_2)
# cProfile.run('variant_2(500)') #1    0.001    0.001    0.023    0.023 task_1.py:49(variant_2)
# cProfile.run('variant_2(1000)') #1    0.001    0.001    0.045    0.045 task_1.py:49(variant_2)
# cProfile.run('variant_2(2000)') #1    0.005    0.005    0.091    0.091 task_1.py:49(variant_2)
# cProfile.run('variant_2(4000)') #1    0.004    0.004    0.192    0.192 task_1.py:49(variant_2)
# cProfile.run('variant_2(8000)') #1    0.008    0.008    0.378    0.378 task_1.py:49(variant_2)
# cProfile.run('variant_2(50000)') #1    0.039    0.039    1.932    1.932 task_1.py:51(variant_2)

print('-' * 50)
# Вариант 3
def variant_3(size):
    max_num = 1000
    min_num = -1000
    lst = [random.randint(min_num, max_num) for i in range(size)]
    min_item = int
    for i in range(min_num, 0):
        if i in lst:
            min_item = i

    if min_item in lst:
        return f'массив: {lst}\n' \
               f'макс. отриц число: {min_item}\n' \
               f'индескс макс. отриц. числа: {lst.index(min_item)}'
    else:
        return f'массив: {lst}\n' \
               f'в массиве нет отицательных чисел'


# print(timeit.timeit('variant_3(10)', number = 100, globals=globals())) #0.1292844630079344
# print(timeit.timeit('variant_3(100)', number = 100, globals=globals())) #1.269007675931789
# print(timeit.timeit('variant_3(250)', number = 100, globals=globals())) #1.861961216898635
# print(timeit.timeit('variant_3(500)', number = 100, globals=globals())) #3.6216965339845046
# print(timeit.timeit('variant_3(1000)', number = 100, globals=globals())) #6.625451817992143
# print(timeit.timeit('variant_3(2000)', number = 100, globals=globals())) #11.032342099002562
# print(timeit.timeit('variant_3(4000)', number = 100, globals=globals())) #16.81063415203243
# print(timeit.timeit('variant_3(8000)', number = 100, globals=globals())) #23.372876806068234
# print(timeit.timeit('variant_3(50000)', number = 100, globals=globals())) #68.05353865301004
# print(timeit.timeit('variant_3(75000)', number = 100, globals=globals())) #94.19080322000082

# cProfile.run('variant_3(10)') #1    0.001    0.001    0.006    0.006 task_1.py:88(variant_3)
# cProfile.run('variant_3(100)') # 1    0.011    0.011    0.022    0.022 task_1.py:88(variant_3)
# cProfile.run('variant_3(250)') #1    0.027    0.027    0.053    0.053 task_1.py:88(variant_3)
# cProfile.run('variant_3(500)') # 1    0.041    0.041    0.090    0.090 task_1.py:88(variant_3)
# cProfile.run('variant_3(1000)') #1    0.072    0.072    0.163    0.163 task_1.py:88(variant_3)
# cProfile.run('variant_3(2000)') # 1    0.121    0.121    0.262    0.262 task_1.py:88(variant_3)
# cProfile.run('variant_3(4000)') #1    0.222    0.222    0.555    0.555 task_1.py:88(variant_3)
# cProfile.run('variant_3(8000)') # 1    0.160    0.160    0.609    0.609 task_1.py:88(variant_3)
# cProfile.run('variant_3(50000)') #1    0.147    0.147    2.057    2.057 task_1.py:92(variant_3)

#Выводы
# Сложность линейная. Второй вариант является самым быстрым из 3-х вариантов,
# за счет того, что избавился от второго цикла в первом варианте.
#Тестировал на одном диапазоне чисел, но в вариант3, если протестирвать
# с узким диапазоном показывает результаты быстрее. В 3-м варианте чем
# шире диапазон отриц. чисел, тем медленнее обрабатывает.