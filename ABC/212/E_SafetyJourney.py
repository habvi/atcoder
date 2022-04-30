from collections import defaultdict

n, m, K = map(int, input().split())
MOD = 998244353

ng = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    ng[a].append(b)
    ng[b].append(a)

dp = [0] * n
dp[0] = 1
for _ in range(K):
    ndp = [0] * n
    total = sum(dp) % MOD
    for v in range(n):
        ndp[v] += total - dp[v]
        for nv in ng[v]:
            ndp[v] -= dp[nv]

        ndp[v] %= MOD
    dp = ndp

print(dp[0])