from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
MOD = 998244353

dp = [0] * 3001
for i in range(a[0], b[0] + 1):
    dp[i] += 1
dp = list(accumulate(dp))

for i in range(1, n):
    ndp = [0] * 3001
    for j in range(a[i], b[i] + 1):
        ndp[j] = dp[j] % MOD
    dp = list(accumulate(ndp))
print(dp[b[-1]] % MOD)