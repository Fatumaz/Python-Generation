def gcd(a, b):
    # while a != 0 and b != 0:
    #     if a >= b:
    #         a %= b
    #     else:
    #         b %= a
    # return a or b
    if a == 0:
        return b
    return gcd(b % a, a)

def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()