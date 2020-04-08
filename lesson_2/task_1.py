#1. Написать программу, которая будет складывать, вычитать, умножать
# или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а
# должна запрашивать новые данные для вычислений. Завершение программы
# должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак
# операции. Также сообщать пользователю о невозможности деления на
# ноль, если он ввел 0 в качестве делителя.
def counting():
    while True:
        quit = input('Для продолжения работы программы нажмите '
                     'любую клавишу, а для выхода нажмите клавишу - "q": ')
        if quit == 'q':
            print('Конец программы!')
            break
        else:
            num_1 = float(input('Введите первое число: '))
            num_2 = float(input('Введите второе число: '))
            action = input('Введите математический знак:\n " * " - для умножения\n" / " - для деления\n'
                           '" + " - для сложения\n" - " - для вычитания: ')
            def check_action(action):
                if action == '*':
                    print(f'{num_1} * {num_2} = {round(num_1 * num_2, 3)}')
                elif action == '/':
                    try:
                        print (f'{num_1} / {num_2} = {round(num_1 / num_2, 3)}')
                    except ZeroDivisionError:
                        print ('деление на ноль!')
                elif action == '+':
                    print(f'{num_1} + {num_2} = {num_1 + num_2}')
                elif action == '-':
                    print(f'{num_1} - {num_2} = {num_1 - num_2}')
                else:
                    action = False
                    while action != True:
                        action = input('Введите математический знак: " * " - для умножения\n " / " - для деления\n'
                               '" + " - для сложения\n " - " - для вычитания: ')
                        check_action(action)
                        action = True
            check_action(action)


counting()

# Вариант без внутренней функции
def counting():
    while True:
            quit = input('Для продолжения работы программы нажмите '
                         'любую клавишу, а для выхода нажмите клавишу - "q": ')
            if quit == 'q':
                print('Конец программы!')
                break
            else:
                num_1 = float(input('Введите первое число: '))
                num_2 = float(input('Введите второе число: '))
                action = input('Введите математический знак:\n " * " - для умножения\n" / " - для деления\n'
                             '" + " - для сложения\n" - " - для вычитания: ')
                if action == '*':
                    print(f'{num_1} * {num_2} = {round(num_1 * num_2, 3)}')
                elif action == '/':
                    try:
                        print(f'{num_1} / {num_2} = {round(num_1 / num_2, 3)}')
                    except ZeroDivisionError:
                        print('деление на ноль!')
                elif action == '+':
                    print(f'{num_1} + {num_2} = {num_1 + num_2}')
                elif action == '-':
                    print(f'{num_1} - {num_2} = {num_1 - num_2}')
                else:
                    action = False
                    while action != True:
                        action = input('Введите математический знак: " * " - для умножения\n " / " - для деления\n'
                               '" + " - для сложения\n " - " - для вычитания: ')
                        if action == '*' or action == '/' or action == '+' or action == '-':
                            if action == '*':
                                print(f'{num_1} * {num_2} = {round(num_1 * num_2, 3)}')
                            elif action == '/':
                                try:
                                    print(f'{num_1} / {num_2} = {round(num_1 / num_2, 3)}')
                                except ZeroDivisionError:
                                    print('деление на ноль!')
                            elif action == '+':
                                print(f'{num_1} + {num_2} = {num_1 + num_2}')
                            else:
                                print(f'{num_1} - {num_2} = {num_1 - num_2}')
                            action = True

# counting()


