text = input()
count = 0
for c in text:
    if c.isdigit():
        count += 1
print(count)