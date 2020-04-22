# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Задача
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).

# Вариант 1
number = input('Введите любое натуральное число: ')
even_dij = str()
odd_dij = str()
for i in number:
    i = int(i)
    if i % 2 == 0:
        even_dij += str(i)
    else:
        odd_dij += str(i)

print(f'кол-во четных цифр: {len(even_dij)}, '
      f'четные: {" ".join(even_dij)}\n'
      f'кол-во нечетных цифр {len(odd_dij)}, '
      f'нечетные: {" ".join(odd_dij)}')

# Вариант 2
number = input('Введите любое натуральное число: ')
nechet = []
chet = []
for i in number:
    chet.append(i) if int(i) % 2 == 0 else nechet.append(i)

print('кол-во четных цифр:', len(chet), ', четные: ', *chet, '\n'
      'кол-во нечетных цифр:', len(nechet), ', нечетные: ', *nechet)

# Вариант 3
number = list(input('Введите любое натуральное число: '))
num_chet = [i for i in number if int(i) % 2 == 0]
num_nech = [i for i in number if int(i) % 2 != 0]

print('кол-во четных цифр:', len(num_chet), ', четные: ', *num_chet, '\n'
      'кол-во нечетных цифр:', len(num_nech),', нечетные: ', *num_nech)

import sys
def sum_mem(*args):
    sum_ = 0
    for i in [*args]:
        sum_size = sys.getsizeof(i)
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for key, value in i.items():
                    sum_size += sys.getsizeof(key)
                    sum_size += sys.getsizeof(value)
            elif not isinstance(i, str):
                for item in i:
                    sum_size += sys.getsizeof(item)
        sum_ += sum_size
    return sum_

print('Итого памяти по варианту 1: ', sum_mem(number, even_dij, odd_dij, len(even_dij), len(odd_dij)))
print('Итого памяти по варианту 2: ', sum_mem(number, nechet, chet, len(nechet), len(chet)))
print('Итого памяти по варианту 3: ', sum_mem(number, num_chet, num_nech, len(num_chet), len(num_nech)))

#Выводы:
#версия pyhon 3.7.3, разрядность ОС Х86_64
#для теста по всем трем вариантам вводилось число 1234567890
#Итого памяти по варианту 1:  864
#Итого памяти по варианту 2:  1512
#Итого памяти по варианту 3:  1512
#1-ый вариант экономичнее потому, что строка занимает меньше памяти
# чем список
