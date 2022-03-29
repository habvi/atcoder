from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

m = 3000
dp = [1] * (m + 1)
for a, b in zip(A, B):
    ndp = [0] * (m + 1)
    for i in range(a, b + 1):
        ndp[i] += dp[i]
        ndp[i] %= MOD
    dp = list(accumulate(ndp))

print(dp[B[-1]] % MOD)