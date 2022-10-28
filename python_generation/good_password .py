import string


# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    count = 0
    for symbols in (digits, lowers, uppers):
        if any(c in symbols for c in password):
            count += 1
            continue
    if count == 3:
        return True
    return False if count == 1 else False



# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))


if __name__ == '__main__':
    assert is_password_good('') == 'Too Weak'
    assert is_password_good('1234567') == 'Too Weak'
    assert is_password_good('qwertyu') == 'Too Weak'
    assert is_password_good('QAZWSXE') == 'Too Weak'
    assert is_password_good('QAaa1') == 'Too Weak'
    assert is_password_good('12345678') == 'Weak'
    assert is_password_good('123456789101112') == 'Weak'
    assert is_password_good('qwertyurfvrgt') == 'Weak'
    assert is_password_good('QAZWSXEDCTGB') == 'Weak'
    assert is_password_good('1234rfvr') == 'Good'
    assert is_password_good('1234rfvrujmi') == 'Good'
    assert is_password_good('1234CTGB') == 'Good'
    assert is_password_good('1234CTGBWS') == 'Good'
    assert is_password_good('CTGBWSrfvr') == 'Good'
    assert is_password_good('GBWSrfvr') == 'Good'
    assert is_password_good('123GBWSrfvr') == 'Very Good'
    assert is_password_good('123456Wr') == 'Very Good'
    assert is_password_good('qwertyfZ1') == 'Very Good'
