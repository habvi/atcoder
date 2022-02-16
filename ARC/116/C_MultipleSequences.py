from collections import defaultdict

def Sieve(x):
    memo = [0] * (x + 1)
    for i in range(2, x + 1):
        if memo[i]:
            continue
        memo[i] = i
        for j in range(i * i, x + 1, i):
            if memo[j]:
                continue
            memo[j] = i
    return memo

def comb(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    nmrt = fact[n]
    dnmnt = invfact[n - r] * invfact[r] % MOD
    return nmrt * dnmnt % MOD


n, m = map(int, input().split())
MOD = 998244353

lenc = 3 * 10**5
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

memo = Sieve(m)

ans = 0
for i in range(1, m + 1):
    pfact = defaultdict(int)
    rev = i
    while rev > 1:
        pfact[memo[rev]] += 1
        rev //= memo[rev]

    total = 1
    for v in pfact.values():
        total *= comb(n - 1 + v, v, MOD)
        total %= MOD

    ans += total
    ans %= MOD

print(ans)