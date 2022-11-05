# объявление функции
def number_to_words(num):
    list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    list_11 = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
               'семнадцать',
               'восемнадцать', 'девятнадцать']
    list_21 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num // 10 == 0:
        return list_1[num - 1]
    elif num // 10 == 1:
        return list_11[num - 10]
    elif num % 10 == 0:
        return list_21[num // 10 - 2]
    else:
        return (f'{list_21[num // 10 - 2]} {list_1[num % 10 - 1]}')


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
# if __name__ == '__main__':
#     assert number_to_words(1) == 'один'
#     assert number_to_words(3) == 'три'
#     assert number_to_words(10) == 'десять'
#     assert number_to_words(16) == 'шестнадцать'