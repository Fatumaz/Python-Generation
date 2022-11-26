def fib(n):
    digit = [0, 1]
    for i in range(2, n + 1):
        digit.append(digit[i - 1] + digit[i - 2])
    return digit[-1]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    assert fib(1) == 0
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(10) == 5
    assert fib(11) == 89
    assert fib(19) == 144
    assert fib(20) == 6765
