from decimal import Decimal

def declination(x, y):
    if x > 1:
        return (Decimal(y - 1) / x, Decimal(y) / (x - 1))
    else:
        return (Decimal(y - 1) / x, float('inf'))


n = int(input())
z = []
for _ in range(n):
    x, y = map(int, input().split())
    z.append(declination(x, y))

z.sort(key=lambda x : x[1])

ans = 0
right = -1
for l, r in z:
    if right <= l:
        ans += 1
        right = r
print(ans)