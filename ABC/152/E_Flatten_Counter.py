from collections import Counter

def Sieve(x):
    memo = [0] * (x + 1)
    for i in range(2, x + 1):
        if memo[i]: continue
        memo[i] = i
        for j in range(i * i, x + 1, i):
            if memo[j]: continue
            memo[j] = i
    return memo


n = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7
memo = Sieve(max(A))

def pfact(x):
    pfct = []
    while x > 1:
        pfct.append(memo[x])
        x //= memo[x]
    return pfct

c = Counter()
for a in A:
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