_ = input()

base = 100
ans = []
for power in range(3):
    x = base ** power
    for i in range(1, base):
        ans.append(x * i)
print(len(ans))
print(*ans)
