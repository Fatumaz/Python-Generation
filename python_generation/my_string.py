word = input()
centre = (len(word) + 1) // 2

print(word[centre:] + word[:centre])
