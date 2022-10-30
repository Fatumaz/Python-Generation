# объявление функции
def is_correct_bracket(text):
    while text.find('()') >= 0:
        text = text.replace('()', '')
    return (len(text) == 0)


# считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))

# Посчитать кол-во '('
# Посчитать кол-во ')'
# Сравнить кол-во '(' с ')'

if __name__ == '__main__':
    assert is_correct_bracket('((()))') == True
    assert is_correct_bracket('(()())') == True
    assert is_correct_bracket('(())()') == True
    assert is_correct_bracket('()(())') == True
    assert is_correct_bracket('()()()') == True
    assert is_correct_bracket('()(())()()()(())()(()())((()))') == True
    assert is_correct_bracket('()(())()(()())((()))()(())') == True
    assert is_correct_bracket('())()()()(') == False
    assert is_correct_bracket(')))(((') == False
    assert is_correct_bracket('()(())()((())((()))()(())') == False
    assert is_correct_bracket('()(())()(()())((()))()(()') == False
    assert is_correct_bracket(')(())()(()())((()))()(())') == False
    assert is_correct_bracket('())(()') == False
    assert is_correct_bracket(')))') == False
    assert is_correct_bracket('((((') == False
    assert is_correct_bracket('())((((())))') == False

