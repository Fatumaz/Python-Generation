# объявление функции
def draw_triangle():
    spaces_str = 7
    stars_str = 1
    for i in range(8):
        print(f'{" " * spaces_str}{"*" * stars_str}')
        spaces_str -= 1
        stars_str += 2
# основная программа
draw_triangle()  # вызов функции