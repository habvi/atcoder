x, y = map(int, input().split())

p = [0, 300_000, 200_000, 100_000]

ans = 400_000 * (x == y == 1)
if x <= 3:
    ans += p[x]
if y <= 3:
    ans += p[y]

print(ans)