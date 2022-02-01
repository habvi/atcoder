h, w = map(int, input().split())
A = [input() for _ in range(h)]
MOD = 10**9 + 7

dp = [[0] * w for _ in range(h)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if A[i][j] == '#':
            continue
        
        if i != h - 1 and A[i + 1][j] != '#':
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
        if j != w - 1 and A[i][j + 1] != '#':
            dp[i][j + 1] += dp[i][j]
            dp[i][j + 1] %= MOD

print(dp[-1][-1])