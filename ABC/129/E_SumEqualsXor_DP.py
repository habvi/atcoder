L = input()
n = len(L)
MOD = 10**9 + 7

# yet, free
dp = [1, 0]
for bit in L:
    ndp = [0, 0]
    if bit == '0':
        ndp[0] = dp[0]
        ndp[1] = dp[1]
    else:
        ndp[1] += sum(dp)

    if bit == '0':
        ndp[1] += dp[1] * 2
    else:
        ndp[0] += dp[0] * 2
        ndp[1] += dp[1] * 2

    ndp[0] %= MOD
    ndp[1] %= MOD
    dp = ndp

print(sum(dp) % MOD)