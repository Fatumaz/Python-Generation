s = input()
if s.count('f') == 0:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
