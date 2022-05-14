W = int(input())

W = int(input())
ans = []
base = 100
for exp in range(3):
    x = 100 ** exp
    for i in range(1, 100):
        ans.append(x * i)

print(len(ans))
print(*ans)