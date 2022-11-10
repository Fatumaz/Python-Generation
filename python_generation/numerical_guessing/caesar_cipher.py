original = 'Блажен, кто верует, тепло ему на свете!'
right_shift = 10
encrypted = ''


for c in original:
    if c.isalpha():
        encrypted = ord(c) + right_shift # индекс + ключ
        if ord(c) > 1103 or (c.isupper() and ord(c) >= 1071): # Если индекс больше предела регистра, то начать сначала алфавита
            encrypted -= 32
        print(chr(encrypted), end='')
    else:
        print(c, end='')


