#6.  В программе генерируется случайное целое число от 0 до 100. Пользователь должен
# его отгадать не более чем за 10 попыток. После каждой неудачной
# попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.

import random

rand_num = random.randint(0, 100)
count = 0
guess_try = 10
while count < guess_try:
    count += 1
    user_num = int(input('Введите число от 0 до 100: '))
    if count == guess_try:
        print(f'Вы не угадали. Загаданное число - {rand_num}\n '
              f'Игра окончена.')
    else:
        if user_num == rand_num:
            print('Поздравляем, вы угадали!')
            break
        elif user_num > rand_num:
            print(f'Введенное число {user_num} больше загаданного.\n'
                  f'У вас осталось {guess_try - count} попыток')
        else:
            print(f'Введенное число {user_num} меньше загаданного.\n'
                  f'У вас осталось {guess_try - count} попыток')

