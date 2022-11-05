from math import factorial
# объявление функции
def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# считываем данные
# n = int(input())
# k = int(input())
#
# # вызываем функцию
# print(compute_binom(n, k))

if __name__ == '__main__':
    assert compute_binom(1, 1) == 1
    assert compute_binom(2, 1) == 2
    assert compute_binom(10, 2) == 45
    assert compute_binom(15, 2) == 105
    assert compute_binom(100, 3) == 161700
    assert compute_binom(64, 7) == 621216192
