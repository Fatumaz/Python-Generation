right_shift = 1


def encryption(text, right_shift):
    for c in text:
        if not c.isalpha():
            print(c, end='')

        encrypted = ord(c) + right_shift  # индекс + ключ

        if 64 < ord(c) < 91 or 96 < ord(c) < 123:
            # Если индекс >= "Z" или "z", то продолжить сначала алфавита
            if encrypted > 122 or (c.isupper() and encrypted > 90):
                encrypted -= 26
            print(chr(encrypted), end='')

        if 1039 < ord(c) < 1104:
            # Если индекс > "я" или "Я", то продолжить сначала алфавита
            if encrypted > 1103 or (c.isupper() and encrypted > 1071):
                encrypted -= 32
            print(chr(encrypted), end='')


def decoding(text, right_shift):
    for c in text:
        if not c.isalpha():
            print(c, end='')
            continue
        encrypted = ord(c) - right_shift  # индекс + ключ

        if 64 < ord(c) < 91 or 96 < ord(c) < 123:
            if encrypted <= 64 or (c.islower() and encrypted <= 96):
                encrypted += 26
            print(chr(encrypted), end='')
            continue

        if 1039 < ord(c) < 1104:
            if encrypted < 1040 or (c.islower() and encrypted < 1072):
                encrypted += 32
            print(chr(encrypted), end='')


def shift(word):
    total = 0
    for c in word:
        if c.isalpha():
            total += 1
    return total


text = input('Введи текст:\n')
question = input('Зашифровать или расшифровать? 0/1\n')


if question == '0':
    for c in text.split():
        right_shift = shift(c)
        encryption(c, right_shift)
        print(' ', end='')

if question == '1':
    total = 0
    while right_shift <= 26:
        right_shift += 1
        total += 1
        decoding(text, right_shift)
        print(" -", total)
