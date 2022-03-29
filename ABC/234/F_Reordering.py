from collections import Counter

def comb(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    r = min(r, n - r)
    nmrt = fact[n]
    dnmnt = invfact[n - r] * invfact[r] % MOD
    return nmrt * dnmnt % MOD


S = input()
n = len(S)
MOD = 998244353

lenc = n + 5
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD


dp = [0] * (n + 1)
dp[0] = 1
for _, num in Counter(S).items():
    ndp = [0] * (n + 1)
    for new in range(num + 1):
        for pre in range(n + 1):
            total = pre + new
            if total <= n:
                ndp[total] += dp[pre] * comb(total, new, MOD)
                ndp[total] %= MOD
    dp = ndp

print((sum(dp) - 1 + MOD) % MOD)