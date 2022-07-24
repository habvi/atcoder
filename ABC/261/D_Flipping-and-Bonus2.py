from collections import defaultdict

n, m = map(int, input().split())
X = list(map(int, input().split()))

bonus = defaultdict(int)
for _ in range(m):
    c, y = map(int, input().split())
    bonus[c] = y

INF = float('inf')
dp = [-INF] * (n + 1)
dp[0] = 0
for i, x in enumerate(X):
    ndp = [-INF] * (n + 1)
    for j in range(n + 1):
        ndp[0] = max(ndp[0], dp[j])
        if j < n:
            ndp[j + 1] = dp[j] + x + bonus[j + 1]
    dp = ndp
print(max(dp))