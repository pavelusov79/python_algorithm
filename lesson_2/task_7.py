#7. Напишите программу, доказывающую или проверяющую, что для
# множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def check_theor(n):
    def check_left(n):
        if n == 1:
            return 1
        return n + check_left(n - 1)
    check_left(n)
    if check_left(n) == n * (n + 1) / 2:
        return True
    else:
        return False


print(check_theor(112))

# Или
def check(n):
    if n == 1:
        return 1
    else:
        return n + check(n - 1)


def check_theorem(n):
    if check(n) == n * (n + 1) / 2:
        return True
    else:
        return False


print(check_theorem(12))


# Вариант 2
def check_theorema(n):
    if sum(range(1, n + 1)) == n * (n + 1) / 2:
        return True
    else:
        return False


print(check_theorema(20))



