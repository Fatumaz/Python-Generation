# В переменных high и low хранятся границы части списка в котором ищем
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high: # Пока эта часть не сократится до одного элемента...
        mid = int((low + high) / 2) # ...проверяем средний элемент
        guess = list[mid]
        if guess == item: # Если значение найдено
            return mid
        if guess > item: # Если много
            high = mid - 1
        else:            # Если мало
            low = mid + 1
    return None          # Если значение не существует


my_list = [1, 3, 5, 7, 9]      # Тест

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
