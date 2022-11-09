from random import shuffle, sample

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous_characters = 'il1Lo0O'
chars = ''
total = 0

def checking_conditions(qwst):  # Проверка выбора
    return qwst.lower() in ('y', 'д')

def generate_password(password_length, chars):  # Генерация пароля
    return sample(chars, password_length)

def update_chars(lst, qwst): # Смешивает симовлы и выдаёт строку
    if checking_conditions(qwst):
        digits_lst = list(lst)
        shuffle(digits_lst)
        return ''.join(digits_lst)
    return ''

'''Начало программы'''
while True:
    quantity_passwords = int(input('Укажите необходимое количество паролей\n'))
    password_length = int(input('Какая должна быть длина пароля?\n'))
    qwst_digits = input('Добавить цифры: 0123456789 ?\n')
    qwst_uppercase_letters = input('Добавить прописные буквы: ABCDEFGHIJKLMNOPQRSTUVWXYZ ?\n')
    qwst_lowercase_letters = input('Добавить прописные буквы: abcdefghijklmnopqrstuvwxyz ?\n')
    qwst_punctuation = input('Добавить символы: !#$%&*+-=?@^_ ?\n')
    qwst_ambiguous_characters = input('Использовать символы: il1Lo0O ?\n')

    # Заполнение библиотеки из выбранных символов
    chars += update_chars(digits, qwst_digits)
    chars += update_chars(uppercase_letters, qwst_uppercase_letters)
    chars += update_chars(lowercase_letters, qwst_lowercase_letters)
    chars += update_chars(punctuation, qwst_punctuation)

    # Проверка выбрано ли хоть одно условие
    if chars == '':
        print('Нужно выбрать хоть один модуль')
        continue

    # Проверка символов на исключение из пароля
    if not checking_conditions(qwst_ambiguous_characters):
        chars = chars.replace(str(ambiguous_characters.split()), '')

    # Вывод готовых паролей
    for i in range(quantity_passwords):
        print(''.join(generate_password(password_length, chars)))
    quit()
