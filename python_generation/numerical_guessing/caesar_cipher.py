ru_encrpt = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
en_encrpt = 'To be, or not to be, that is the question!'
right_shift = 25
ru_dscrpt = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
en_dscrpt = "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd."

# en_dscrpt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# en_dscrpt = 'abcdefghijklmnopqrstuvwxyz'

def rus_encryption(text, right_shift):
    for c in text:
        if c.isalpha():
            encrypted = ord(c) + right_shift  # индекс + ключ
            if encrypted > 1103 or (
                    c.isupper() and encrypted > 1071):  # Если индекс > "я" или "Я", то продолжить сначала алфавита
                encrypted -= 32
            print(chr(encrypted), end='')
        else:
            print(c, end='')


def en_encryption(text, right_shift):
    for c in text:
        if c.isalpha():
            encrypted = ord(c) + right_shift  # индекс + ключ
            if (
                    c.isupper() and encrypted > 90) or encrypted > 122:  # Если индекс >= "Z" или "z", то продолжить сначала алфавита
                encrypted -= 26
            print(chr(encrypted), end='')
        else:
            print(c, end='')


def ru_decoding(text, right_shift):
    for c in text:
        if c.isalpha():
            encrypted = ord(c) - right_shift  # индекс + ключ
            if encrypted < 1040 or (
                    c.islower() and encrypted < 1072):  # Если индекс > "а" или "А", то продолжить сначала алфавита
                encrypted += 32
            print(chr(encrypted), end='')
        else:
            print(c, end='')

def en_decoding(text, right_shift):
    for c in text:
        if c.isalpha():
            encrypted = ord(c) - right_shift  # индекс + ключ
            if encrypted <= 64 or (c.islower() and encrypted <= 96):  # Если индекс > "а" или "А", то продолжить сначала алфавита
                encrypted += 26
            print(chr(encrypted), end='')
        else:
            print(c, end='')


en_decoding(en_dscrpt, right_shift)
