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

class FastComb:
    def __init__(self, max_nr, mod):
        self.mod = mod
        self.fact = [1] * max_nr
        self.invfact = [1] * max_nr

        for i in range(1, max_nr):
            self.fact[i] = self.fact[i - 1] * i % self.mod

        self.invfact[max_nr - 1] = pow(self.fact[max_nr - 1], self.mod - 2, self.mod)
        for i in range(max_nr - 1, 0, -1):
            self.invfact[i-1] = self.invfact[i] * i % self.mod

    def comb(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        r = min(r, n - r)
        nmrt = self.fact[n]
        dnmnt = self.invfact[n - r] * self.invfact[r] % self.mod
        return nmrt * dnmnt % self.mod


n, m = map(int, input().split())
MOD = 998244353

max_nr = 3 * 10**5
f = FastComb(max_nr, MOD)

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
        total *= f.comb(n - 1 + v, v)
        total %= MOD

    ans += total
    ans %= MOD

print(ans)