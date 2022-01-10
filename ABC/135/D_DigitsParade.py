S = input()
MOD = 10**9 + 7
dp = [0] * 13
dp[0] = 1
b = 1
for s in S[::-1]:
    ndp = [0] * 13
    if s == '?':
        for k in range(10):
            for i in range(13):
                idx = (k*b + i) % 13
                ndp[idx] += dp[i]
                ndp[idx] %= MOD
    else:
        s = int(s)
        for i in range(13):
            idx = (s*b + i) % 13
            ndp[idx] += dp[i]
            ndp[idx] %= MOD
    b *= 10
    b %= 13
    dp = ndp
print(dp[5])