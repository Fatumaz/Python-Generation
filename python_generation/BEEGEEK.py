# объявление функции
def is_valid_password(password):
    password = password.split(':')
    if password[0] == password[0][::-1] and int(password[2]) % 2 == 0 and len(
            [i for i in range(1, int(password[1]) + 1) if int(password[1]) % i == 0]) == 2 and len(password) == 3:
        return True
    else:
        return False


# считываем данные
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))

# Разделить на список
# проверить на палиндром часть [0]
# проверить [1] что делится только на себя
# проветь [2] четное

if __name__ == '__main__':
    assert is_valid_password('15551:7:290') == True
    assert is_valid_password('155561:7:290') == False
    assert is_valid_password('15551:72:290') == False
    assert is_valid_password('15551:7:291') == False
    assert is_valid_password('155351:70:290') == False
    assert is_valid_password('1551151:700:2901') == False
    assert is_valid_password('11111:71:90000') == True
    assert is_valid_password('24422442:181:890000') == True
    assert is_valid_password('1221:101:22:22') == False
    assert is_valid_password('1221:101:22:221221:101:22:22') == False
