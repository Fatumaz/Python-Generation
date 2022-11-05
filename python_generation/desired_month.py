# объявление функции
def get_month(language, number):
    en_month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    ru_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    return en_month[number - 1] if language == 'en' else ru_month[number - 1]



# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))