# объявление функции
def is_one_away(word1, word2):
    if (len(word1) > len(word2)) or (word1 == word2) or (len(word1) < len(word2)):
        return False
    symbol = 0

    for i in range(len(word1)):
        if word1[i] == word2[i]:
            symbol += 1

    if len(word1) - 1 == symbol:
        return True
    else:
        return False


# считываем данные
# txt1 = input()
# txt2 = input()

# вызываем функцию
# print(is_one_away(txt1, txt2))

if __name__ == '__main__':
    assert is_one_away('bike', 'hike') == True
    assert is_one_away('water', 'wafer') == True
    assert is_one_away('abcd', 'abpo') == False
    assert is_one_away('abcd', 'abcde') == False
    assert is_one_away('abcd1234567', 'abcd1234568') == True
    assert is_one_away('abcd', 'abcd') == False
    assert is_one_away('aab', 'aba') == False
    assert is_one_away('abcd', 'dcba') == False
    assert is_one_away('aab', 'abb') == True
