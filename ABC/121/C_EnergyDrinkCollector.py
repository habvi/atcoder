n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

ab.sort()
ans = 0
num = 0
for a, b in ab:
    if num + b >= m:
        ans += (m - num) * a
        break
    ans += a * b
    num += b

print(ans)