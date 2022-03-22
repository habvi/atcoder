s = input()
lens = len(s)
w = 'chokudai'
lenw = len(w)
MOD = 10**9+7
dp = [[0]*(lens+1) for _ in range(lenw+1)]
for i in range(lens+1):
    dp[0][i] = 1

for i in range(1, lenw+1):
    for j in range(1, lens+1):
        dp[i][j] += dp[i][j-1]
        dp[i][j] %= MOD
        if s[j-1] not in w: continue
        if w.index(s[j-1]) == i-1:
            dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= MOD
print(dp[lenw][lens])