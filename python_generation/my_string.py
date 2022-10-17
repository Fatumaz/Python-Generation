lst = []
for _ in range(int(input())):
    text = input()
    if text not in lst:
        lst.append(text)
print(*lst, sep='\n')