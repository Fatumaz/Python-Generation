# объявление функции
def is_pangram(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    if ''.join(sorted(set(text.lower().replace(' ', '')))) == abc:
        return True
    else:
        return False

# считываем данные
# text = input()
#
# # вызываем функцию
# print(is_pangram(text))

if __name__ == '__main__':
    assert is_pangram('Jackdaws love my big sphinx of quartz') == True
    assert is_pangram('The five boxing wizards jump quickly') == True
    assert is_pangram('The quick brown fox jumps over the lazy dog') == True
    assert is_pangram('Crazy Fredrick bought many very exquisite opal jewels') == True
    assert is_pangram('jsdfhsadfhkljsad') == False
    assert is_pangram('Crazy Fredrick bought many very exquisite opal jewel') == True
    assert is_pangram('razy Fredrick bought many very exquisite opal') == False
