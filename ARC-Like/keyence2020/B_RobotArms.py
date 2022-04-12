n = int(input())
xl = []
for _ in range(n):
    x, d = map(int, input().split())
    xl.append((x - d, x + d))

xl.sort(key=lambda x: x[1])

now = -float('inf')
ans = 0
for l, r in xl:
    if now <= l:
        now = r
        ans += 1
print(ans)