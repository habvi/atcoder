n = int(input())
a = list(map(int, input().split()))
x = 0
for i in range(n):
    if i % 2 == 0:
        x += a[i]
    else:
        x -= a[i]

ans = [0] * n
ans[0] = x // 2
for i in range(n - 1):
    ans[i + 1] = a[i] - ans[i]

for i in range(n):
    ans[i] *= 2

print(*ans)