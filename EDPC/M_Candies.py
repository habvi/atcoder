from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7

dp = [0] * (K + 1)
dp[0] = 1
for a in A:
    ndp = [0] * (K + 1)
    dp = [0, *accumulate(dp)]
    for i in range(K + 1):
        r = i + 1
        l = max(0, i - a)
        ndp[i] += dp[r] - dp[l]
        ndp[i] %= MOD
    dp = ndp
print(dp[-1])
