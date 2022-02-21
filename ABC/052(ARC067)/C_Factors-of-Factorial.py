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


n = int(input())
MOD = 10**9 + 7

memo = Sieve(10 ** 3)

pfact = defaultdict(int)
for i in range(2, n + 1):
    while i > 1:
        pfact[memo[i]] += 1
        i //= memo[i]

ans = 1
for num in pfact.values():
    ans *= num + 1
    ans %= MOD

print(ans)