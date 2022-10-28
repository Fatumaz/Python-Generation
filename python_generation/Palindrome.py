# объявление функции
def is_palindrome(text):
    palindrome = [c for c in ''.join(text.lower().split()) if c.isalnum()]
    return palindrome == palindrome[::-1]
# # считываем данные
# txt = input()

# вызываем функцию
# print(is_palindrome(txt))

if __name__ == '__main__':
    assert is_palindrome('А роза упала на лапу Азора') == True
    assert is_palindrome('Standart - smallest, sell Amstrad nats.') == True
    assert is_palindrome('Zoo belt to be Russia, is sure bottle booz.') == True
    assert is_palindrome('Evil fit some kill like me, kill like most, if live.') == True
    assert is_palindrome('Do me?.. Kill I victim? Must summit civil like mod.') == True
    assert is_palindrome('Карман, жена, но Какашкин - вор! О, Ковалева... Вела во коровник. Ша! Как она нежна! рак...') == False
    assert is_palindrome('Зело полз Антипарх то вино пить - тип он и вот храпит - на зло полез') == True
    assert is_palindrome('Марс близ Овна. На базар генерал в ларе негра за банан возил б. Срам!') == True
    assert is_palindrome('Тер жен, а нес токмо радение о бодром мордобое, и недаром кот сена не жрет.') == True
    assert is_palindrome('Тер жен, а нес токмо недаром кот сена не жрет.') == False
    assert is_palindrome('sjdflksjflksdjflsdjk sdlfhsdjfE#R#$$#R !!!!! sdjfnsdjkfnsd kjcvadsk') == False

