s = input()
ls = len(s)
w = 'chokudai'
lw = len(w)
MOD = 10**9 + 7

dp = [[0] * (ls + 1) for _ in range(lw + 1)]
for i in range(ls + 1):
    dp[0][i] = 1

for i in range(1, lw + 1):
    for j in range(1, ls + 1):
        dp[i][j] += dp[i][j - 1]
        dp[i][j] %= MOD
        if s[j - 1] not in w:
            continue
        if w.index(s[j - 1]) == i - 1:
            dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] %= MOD
print(dp[lw][ls])