S = input()
MOD = 10**9 + 7

alph = '?ABC'
dp = [0] * 4
dp[0] = 1
for s in S:
    ndp = dp[:]

    ai = alph.index(s)
    if ai:
        ndp[ai] += dp[ai - 1]
        ndp[ai] %= MOD
    else:
        for i in range(4):
            if i == 0:
                ndp[i] = dp[i] * 3
            else:
                ndp[i] = dp[i] * 3 + dp[i - 1]
            ndp[i] %= MOD
    dp = ndp

print(dp[-1] % MOD)