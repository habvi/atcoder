S = input()
MOD = 10**9 + 7
WORD = 'chokudai'

dp = [0] * 9
dp[0] = 1

for s in S:
    for i, w in enumerate(WORD, 1):
        if s == w:
            dp[i] += dp[i - 1]
            dp[i] %= MOD

print(dp[-1])