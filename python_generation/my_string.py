num = int(input())
count = 0
for i in range(num):
    code = input()
    if code.count('11') >= 3:
        count += 1
print(count)