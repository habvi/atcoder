s = input()
n = len(s)
MOD = 10**9 + 7
dp = [0] * 13
dp[0] = 1
for i in range(n - 1, -1, -1):
    p = pow(10, n - i - 1, 13)
    ndp = [0] * 13

    if s[i] == '?':
        for k in range(10):
            for j in range(13):
                ndp[(k*p + j) % 13] += dp[j]
                ndp[(k*p + j) % 13] %= MOD
    else:
        for j in range(13):
            ndp[(int(s[i])*p + j) % 13] += dp[j]
            ndp[(int(s[i])*p + j) % 13] %= MOD
    dp = ndp
print(dp[5])