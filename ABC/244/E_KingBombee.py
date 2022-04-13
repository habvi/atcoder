from collections import defaultdict

n, m, K, S, T, X = map(int, input().split())
S, T, X = S - 1, T - 1, X - 1
MOD = 998244353

g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

dp = [[0] * 2 for _ in range(n)]
dp[S][0] = 1

for _ in range(K):
    ndp = [[0] * 2 for _ in range(n)]
    for v in range(n):
        for nv in g[v]:
            if nv == X:
                ndp[nv][0] += dp[v][1]
                ndp[nv][1] += dp[v][0]
            else:
                ndp[nv][0] += dp[v][0]
                ndp[nv][1] += dp[v][1]
            ndp[nv][0] %= MOD
            ndp[nv][1] %= MOD
    dp = ndp

print(dp[T][0])