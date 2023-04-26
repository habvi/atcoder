def ceil(a, b):
    return (a + b - 1) // b


N, M = map(int, input().split())
INF = float('inf')

ans = INF
for a in range(1, int(M ** 0.5) + 10):
    b = ceil(M, a)
    if a <= N and b <= N:
        ans = min(ans, a * b)
print(ans if ans != INF else -1)