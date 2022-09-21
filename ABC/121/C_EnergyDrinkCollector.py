N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]

ab.sort()
ans = 0
for a, b in ab:
    x = min(M, b)
    ans += a * x
    M -= x
    if not M:
        break
print(ans)