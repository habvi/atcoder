def Sieve(x):
    memo = [0] * (x + 1)
    primes = []
    for i in range(2, x + 1):
        if memo[i]: continue
        primes.append(i)
        memo[i] = i
        for j in range(i * i, x + 1, i):
            if memo[j]: continue
            memo[j] = i
    return memo, primes

from collections import Counter
n = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7
memo, primes = Sieve(max(A))

def pfact(x):
    pfct = []
    while x > 1:
        pfct.append(memo[x])
        x //= memo[x]
    return pfct

c = Counter(pfact(A[0]))
for a in A[1:]:
    c |= Counter(pfact(a))

lcm = 1
for k, v in c.items():
    lcm *= pow(k, v, MOD)
    lcm %= MOD

inv = 0
for a in A:
    inv += pow(a, MOD - 2, MOD)
    inv %= MOD
print(lcm * inv % MOD)