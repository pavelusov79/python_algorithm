# 5.  Вывести на экран коды и символы таблицы ASCII, начиная с символа
# под номером 32заканчивая 127-м включительно. Вывод выполнить в
# табличной форме: по десять пар "код-символ" в каждой строке.

#Вариант через рекурсию (как вывести по 10 не сумел найти решение)
def num_to_asci(n, m):
    if n == m:
        return f'{n}: "{chr(n)}"'
    return f'{n}: "{chr(n)}" {num_to_asci(n + 1, m)}'


print(num_to_asci(32, 128))

print()
#Вариант 2
string = str()
for el in range(32, 128):
    string += chr(el)
for i in range(0, len(string), 10):
    print(' '.join(string[i:i + 10]))


