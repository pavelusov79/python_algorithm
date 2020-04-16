#2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число. Проанализировать скорость и
# сложность алгоритмов. Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

#Число n (count) - число до которого хотим получить простые числа, ввел
#внутрь функции лишь для удобства тестирования. Эту переменную можно
#вынести за ф-цию, чтобы был вид как по ДЗ seive(k)

import timeit
import cProfile

def seive(k, n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    for el, item in enumerate(res, start=1):
        if k == el:
            return item

# Вариант 2

def sito(num, count):
    simp_lst = [i for i in range(3, count, 2)]
    exclude_lst = []
    for i in simp_lst:
        for j in range(3, i, 2):
            if i % j == 0:
                exclude_lst.append(i)
                break

    simp_lst.insert(0, 2)
    lst = tuple(i for i in simp_lst if i not in exclude_lst)
    for el, item in enumerate(lst, start= 1):
        if num == el:
            return item


# ----------------------------------------------------
# n = 100
# print(timeit.timeit('seive(20, 100)', number = 100, globals = globals()))#0.028324307000730187
# n = 500
# print(timeit.timeit('seive(330, 500)', number = 100, globals = globals()))#0.0847595819941489
#n = 1000
# print(timeit.timeit('seive(500, 1000)', number = 100, globals = globals()))#0.21318349899956957
# n = 2500
# print(timeit.timeit('seive(1200, 2500)', number = 100, globals = globals()))#0.4660950929974206
# n = 5000
# print(timeit.timeit('seive(1234, 5000)', number = 100, globals = globals()))#1.105608376004966
# n = 10000
# print(timeit.timeit('seive(2015, 10000)', number = 100, globals = globals()))#2.1825632870022673

# cProfile.run('seive(20, 100)')#1    0.000    0.000    0.000    0.000 task_2.py:10(seive)
# cProfile.run('seive(330, 500)')#1    0.001    0.001    0.001    0.001 task_2.py:10(seive)
# cProfile.run('seive(500, 1000)')#1    0.001    0.001    0.002    0.002 task_2.py:10(seive)
# cProfile.run('seive(1200, 2500)')# 1    0.004    0.004    0.005    0.005 task_2.py:10(seive)
# cProfile.run('seive(1234, 5000)')#1    0.008    0.008    0.009    0.009 task_2.py:10(seive)
# cProfile.run('seive(2015, 10000)')#1    0.016    0.016    0.020    0.020 task_2.py:10(seive)


# n = 100
# print(timeit.timeit('sito(20, 100)', number = 100, globals = globals()))#0.04410574000212364
# n = 500
# print(timeit.timeit('sito(330, 500)', number = 100, globals = globals()))#0.6108090240013553
#n = 1000
# print(timeit.timeit('sito(500, 1000)', number = 100, globals = globals()))#2.154505408994737
# n = 2500
# print(timeit.timeit('sito(1200, 2500)', number = 100, globals = globals()))#12.452694396997686
# n = 5000
# print(timeit.timeit('sito(1234, 5000)', number = 100, globals = globals()))#48.464349892004975
# n = 10000
# print(timeit.timeit('sito(2015, 10000)', number = 100, globals = globals()))#186.8442319129972

# cProfile.run('sito(20, 100)')#26    0.000    0.000    0.000    0.000 task_2.py:36(<genexpr>)
# cProfile.run('sito(330, 500)')#96    0.002    0.000    0.002    0.000 task_2.py:36(<genexpr>)
# cProfile.run('sito(500, 1000)')#169    0.007    0.000    0.007    0.000 task_2.py:36(<genexpr>)
# cProfile.run('sito(1200, 2500)')#368    0.043    0.000    0.043    0.000 task_2.py:36(<genexpr>)
# cProfile.run('sito(1234, 5000)')#670    0.174    0.000    0.174    0.000 task_2.py:36(<genexpr>)
# cProfile.run('sito(2015, 10000)')#1230    0.690    0.001    0.690    0.001 task_2.py:36(<genexpr>)

#Выводы
# Второе решение - квадратичная сложность. Чем больше число, до которого
# хотим получить простые числа, тем больше времени на обработку - ужасные
#результаты
