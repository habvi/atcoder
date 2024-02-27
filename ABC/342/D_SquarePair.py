from collections import defaultdict

def Sieve(x):
    memo = [0] * (x + 1)
    primes = []
    for i in range(2, x + 1):
        if memo[i]:
            continue
        primes.append(i)
        memo[i] = i
        for j in range(i * i, x + 1, i):
            if memo[j]:
                continue
            memo[j] = i
    return memo, primes

def pfact_dict(x):
    pfct = defaultdict(int)
    while x > 1:
        pfct[memo[x]] += 1
        x //= memo[x]
    return pfct


N = int(input())
A = list(map(int, input().split()))

memo, _ = Sieve(2 * 10**5 + 5)
ans = 0
each_num = defaultdict(int)
for i, a in enumerate(A):
    if a == 0:
        x = 0
        ans += i
    else:
        pf = pfact_dict(a)
        x = 1
        for k, v in pf.items():
            if v % 2:
                x *= k
        ans += (each_num[x] + each_num[0])
    each_num[x] += 1
print(ans)
