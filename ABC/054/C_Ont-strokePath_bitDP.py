n, m = map(int, input().split())
E = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    E[a] |= (1<<b)
    E[b] |= (1<<a)

dp = [[0]*(n) for _ in range(1<<n)]
dp[1][0] = 1
for s in range(1, 1<<n):
    for i in range(n):
        if dp[s][i] == 0: continue
        for j in range(n):
            if i == j: continue
            if (E[i]>>j)&1 == 0: continue
            if (s>>j)&1 == 1: continue
            dp[s|(1<<j)][j] += dp[s][i]
print(sum(dp[-1]))