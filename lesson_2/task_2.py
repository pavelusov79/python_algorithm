# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Введите любое натуральное число: ')
# Вариант 1
even_dijits = str()
odd_dijits = str()
for i in number:
    if i.isdigit():
        i = int(i)
        if i % 2 == 0:
            i = str(i)
            even_dijits += i
        else:
            i = str(i)
            odd_dijits += i

print(f'кол-во четных цифр: {len(even_dijits)}, '
      f'четные: {" ".join(tuple(even_dijits))}\n '
      f'кол-во нечетных цифр {len(odd_dijits)}, '
      f'нечетные: {" ".join(tuple(odd_dijits))}')

# Вариант 2
# m = []
# n = []
# for i in number:
#     if i.isdigit():
#         i = int(i)
#         if i % 2 == 0:
#             n.append(i)
#         else:
#             m.append(i)
#
# print(f'кол-во четных цифр: {len(n)}, четные: {tuple(n)}\n '
#       f'кол-во нечетных цифр {len(m)}, нечетные: {tuple(m)}')
