from collections import defaultdict

N, M, K, S, T, X = map(int, input().split())
S, T, X = S - 1, T - 1, X - 1
MOD = 998244353

g = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

dp = [[0] * N for _ in range(2)]
dp[0][S] = 1
for _ in range(K):
    ndp = [[0] * N for _ in range(2)]
    for v in range(N):
        for nv in g[v]:
            if v == X:
                ndp[0][nv] += dp[1][v]
                ndp[1][nv] += dp[0][v]
            else:
                ndp[0][nv] += dp[0][v]
                ndp[1][nv] += dp[1][v]
            ndp[0][nv] %= MOD
            ndp[1][nv] %= MOD
    dp = [d[:] for d in ndp]
print(dp[0][T])