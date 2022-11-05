# объявление функции
def is_magic(date):
    lst_date = date.split('.')
    if int(lst_date[0]) * int(lst_date[1]) == int(lst_date[2][2:]):
        return True
    else:
        return False
# считываем данные
# date = input()
#
# # вызываем функцию
# print(is_magic(date))

if __name__ == '__main__':
    assert is_magic('10.06.1960') == True
    assert is_magic('15.03.1945') == True
    assert is_magic('03.11.2033') == True
    assert is_magic('03.11.2032') == False
    assert is_magic('15.12.1234') == False
    assert is_magic('10.09.1990') == True

