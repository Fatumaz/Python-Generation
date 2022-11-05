# объявление функции
def get_shipping_cost(quantity):
    total = 1000
    for i in range(1, quantity + 1):
        if i > 1:
            total += 120
    return total

# считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_shipping_cost(n))


if __name__ == '__main__':
    assert get_shipping_cost(1) == 1000
    assert get_shipping_cost(2) == 1120
    assert get_shipping_cost(3) == 1240
    assert get_shipping_cost(100) == 12880
    assert get_shipping_cost(41) == 5800
