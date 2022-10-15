#1 Способ
text = input()[::-1]
later = max(text, key=text.count)
print(later)

#2 Способ
text = input()
count = 0
letter = ''
waste = ''
for c in text:
    if c not in waste:
        waste += c
        if text.count(c) >= count:
            count = int(text.count(c))
            letter = c

print(letter)
