from decimal import Decimal
n = int(input())
z = []
for _ in range(n):
    x, y = map(int, input().split())
    if x > 1:
        a = Decimal(y) / (x - 1)
    else:
        a = float('inf')
    z.append((Decimal(y - 1) / x, a))

z.sort(key=lambda x : x[1])

ans = 0
ok = -1
for i in range(n):
    l, r = z[i]
    if l >= ok:
        ans += 1
        ok = r
print(ans)