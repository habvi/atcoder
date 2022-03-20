from collections import defaultdict

n, m, K, S, T, X = map(int, input().split())
S, T = S - 1, T - 1
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
    for i in range(n):
        for ni in g[i]:
            if ni + 1 == X:
                ndp[ni][0] += dp[i][1]
                ndp[ni][0] %= MOD
                ndp[ni][1] += dp[i][0]
                ndp[ni][1] %= MOD
            else:
                ndp[ni][0] += dp[i][0]
                ndp[ni][0] %= MOD
                ndp[ni][1] += dp[i][1]
                ndp[ni][1] %= MOD
    dp = ndp

print(dp[T][0])