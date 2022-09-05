N = int(input())
mx = 10 ** 5
snuke = [[0] * 5 for _ in range(mx + 1)]
for _ in range(N):
    T, X, A = map(int, input().split())
    snuke[T][X] = A

INF = float('inf')
dp = [-INF] * 5
dp[0] = 0
for t in range(1, mx + 1):
    ndp = [-INF] * 5
    for i in range(5):
        a = snuke[t][i]
        if 0 <= i - 1:
            ndp[i] = max(ndp[i], dp[i - 1] + a)
        ndp[i] = max(ndp[i], dp[i] + a)
        if i + 1 < 5:
            ndp[i] = max(ndp[i], dp[i + 1] + a)
    dp = ndp
print(max(dp))