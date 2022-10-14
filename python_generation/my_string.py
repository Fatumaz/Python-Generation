text = input().upper()

genetic = 'Аденин Гуанин Цитозин Тимин'.split() # создаёт список для перебора
for word in genetic: # Перебирает слова из списка
    print(f'{word}: {text.count(word[:1])}') # Пример вывода: Аденин: 4
