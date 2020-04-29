#1. Определить количество различных подстрок с использованием
# хеш-функции. Задача: на вход функции дана строка, требуется вернуть
# количество различных подстрок в этой строке.
#Примечание:​ в сумму не включаем пустую строку и строку целиком.
import hashlib

def func(s):
    h_str = hashlib.sha1(s.encode('utf-8')).hexdigest()
    sum_ = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            hash_subs = hashlib.sha1(s[i : j].encode('utf-8')).hexdigest()
            if  hash_subs != h_str:
                sum_ += 1

    return sum_


print(func('lamp'))

