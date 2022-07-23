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
    ndp = [0] * (n + 1)
    for j in range(n):
        ndp[j + 1] = dp[j] + x

    for j in range(1, n + 1):
        ndp[j] += bonus[j]

    ndp[0] = max(dp)
    dp = ndp
print(max(dp))