from random import randint


def is_valid(player_number):  # проверка корректности введенных данных
    return player_number.isdigit() and int(player_number) - float(player_number) == 0 < int(player_number) <= 100


def input_num():  # ввод данных
    while True:
        player_number = input()
        if is_valid(player_number):
            return int(player_number)
        else:
            print('А может быть все-таки введем целое число от 1 до ... ваше число')


def comparison_number(right_limit):  # и сравнение с загаданным числом
    digital_random = randint(1, right_limit)
    total = 0
    while True:
        total += 1
        player_number = input_num()
        if player_number < digital_random:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif player_number > digital_random:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угадали, поздравляем!\nКоличество попыток: {total}')
            break


def continid_game():  # Проверка на продолжение
    answer = input(f'\nХотите продолжить?\nВведите "y" или "n":\n ')
    while True:
        if answer.lower() not in ('y', 'д', 'n', 'н'):
            answer = input('Ответ не распознан\nПродолжим ("д"/"н")?\n')
        elif answer.lower() in ('n', 'н'):
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            return False
        else:
            return True


def game():  # Начало
    while True:
        print('\nДобро пожаловать в числовую угадайку!')
        print('Укажите предел диапазона от 1 до ... ваше число')
        right_limit = input_num()
        print(f'Введите число от 1 до {right_limit}')
        comparison_number(right_limit)
        if continid_game():
            continue
        else:
            break


game()  # Запуск игры
