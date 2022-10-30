# объявление функции
def convert_to_python_case(text):
    for c in text:
        if c.isupper():
            text = text.replace(c, '_' + c.lower())
    return text[1:]

# считываем данные
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))

if __name__ == '__main__':
    assert convert_to_python_case('ThisIsCamelCased') == 'this_is_camel_cased'
    assert convert_to_python_case('IsPrimeNumber') == 'is_prime_number'
    assert convert_to_python_case('ConvertToInt32') == 'convert_to_int32'
    assert convert_to_python_case('MyMethodThatDoSomething') == 'my_method_that_do_something'
