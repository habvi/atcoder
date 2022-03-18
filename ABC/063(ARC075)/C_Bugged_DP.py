n = int(input())

dp = 1
total = 0
for _ in range(n):
    s = int(input())
    dp |= dp << s | 1
    total += s

for i in range(total + 1, -1, -1):
    if i % 10 and dp >> i & 1:
        print(i)
        exit()

print(0)