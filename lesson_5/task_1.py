#1. Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех
# предприятий) и отдельно вывести наименования предприятий, чья
# прибыль выше среднего и ниже среднего.

from collections import namedtuple

Firms = namedtuple('Firms', 'name, profit')
n = int(input('Введите число фирм: '))
sum_profit = 0
lst = []
for i in range(n):
    name = input(f'введите название {i + 1}-й фирмы: ')
    profit = [float(input(f'Введите прибыль за {i + 1}-й квартал: ')) for i in range(4)]
    sum_profit += sum(profit)
    firm_i = Firms(name, profit)
    lst.append(firm_i)

for firm in lst:
    if sum(firm.profit) > sum_profit / n:
        print(f'фирма с прибылью за год выше средней прибыли: {firm.name}')
    else:
        print(f'фирма с прибылью за год ниже средней прибыли: {firm.name}')
print(f'средняя прибыль за год по всем фирмам: {round(sum_profit / n, 2)}')

# Вариант 2 без collections
# n = int(input('Введите число фирм: '))
# firms_dict = {}
# sum_prof = 0
# i = 1
# while i <= n:
#     firms_i = input(f'Введите назание {i}-й фирмы: ')
#     firms_dict[firms_i] = [float(input(f'Введите прибыль за {i + 1}-й квартал: ')) for i in range(4)]
#     sum_prof += sum(firms_dict[firms_i])
#     i += 1
#
# for key, item in firms_dict.items():
#     if sum(item) > sum_prof / n:
#         print(f'фирма с прибылью за год выше среднего: {key}')
#     else:
#         print(f'фирма с прибылью за год ниже среднего: {key}')
# print(f'средняя прибыль за год по всем фирмам: {round(sum_prof / n, 2)}')
