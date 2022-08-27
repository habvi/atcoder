N = int(input())
mx = 10 ** 5
hole = {}
for _ in range(N):
    T, X, A = map(int, input().split())
    hole[T] = (X, A)

INF = float('inf')
dp = [-INF] * 5
dp[0] = 0
for now in range(1, mx + 1):
    ndp = [-INF] * 5
    for i in range(5):
        ndp[i] = max(ndp[i], dp[i])
        if i - 1 >= 0:
            ndp[i] = max(ndp[i], dp[i - 1])
        if i + 1 < 5:
            ndp[i] = max(ndp[i], dp[i + 1])
    if now not in hole:
        dp = ndp
        continue
    x, a = hole[now]
    ndp[x] = max(ndp[x], dp[x] + a)
    if x - 1 >= 0:
        ndp[x] = max(ndp[x], dp[x - 1] + a)
    if x + 1 < 5:
        ndp[x] = max(ndp[x], dp[x + 1] + a)
    dp = ndp
print(max(dp))
