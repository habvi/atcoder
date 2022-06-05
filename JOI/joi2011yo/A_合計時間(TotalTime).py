total = 0
for _ in range(4):
    total += int(input())

m, s = divmod(total, 60)
print(m)
print(s)