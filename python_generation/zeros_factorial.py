def factorial(n: int) -> int:
    """принимает неотрицательное число, и возвращает значение факториала данного числа."""
    total = 1
    for digit in range(2, n + 1):
        total *= digit
    return total


def trailing_zeros(n: int) -> int:
    """возвращает сколько нулей на конце факториала"""
    total = 0
    for char in str(factorial(n))[::-1]:
        if char == '0':
            total += 1
        else:
            break
    return total


if __name__ == "__main__":
    assert trailing_zeros(6) == 1
    assert trailing_zeros(10) == 2
    assert trailing_zeros(20) == 4
