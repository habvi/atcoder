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

def pfact_dict(x):
    pfct = defaultdict(int)
    while x > 1:
        pfct[memo[x]] += 1
        x //= memo[x]
    return pfct


n = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

num = defaultdict(int)
memo = Sieve(10**6 + 5)
for a in A:
    for k, v in pfact_dict(a).items():
        num[k] = max(num[k], v)

lcm = 1
for k, v in num.items():
    lcm *= pow(k, v, MOD)
    lcm %= MOD

ans = 0
for a in A:
    ans += lcm * pow(a, MOD - 2, MOD)
    ans %= MOD
print(ans)