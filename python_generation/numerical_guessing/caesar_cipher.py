# ru_encrpt = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ru_encrpt = 'БВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯА'
en_encrpt = 'To be, or not to be, that is the question!'
right_shift = 7
ru_dscrpt = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
en_dscrpt = "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd."


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

        encrypted = ord(c) - right_shift  # индекс + ключ

        if 64 < ord(c) < 91 or 96 < ord(c) < 123:
            if encrypted <= 64 or (c.islower() and encrypted <= 96):
                encrypted += 26
            print(chr(encrypted), end='')

        if 1039 < ord(c) < 1104:
            if encrypted < 1040 or (c.islower() and encrypted < 1072):
                encrypted += 32
            print(chr(encrypted), end='')


# encryption(ru_encrpt, right_shift)
# print()
decoding(ru_dscrpt, right_shift)

# while right_shift < 25:
#     right_shift += 1
#     en_decoding(en_dscrpt, right_shift)
#     print()
