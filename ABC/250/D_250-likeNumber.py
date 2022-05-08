from bisect import bisect

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
    return primes


n = int(input())

primes = Sieve(int(n ** (1 / 3)) + 1)

ans = 0
for p in primes:
    if 2 * p ** 3 > n:
        continue

    ans += bisect(primes, min(p - 1, n // p**3))
print(ans)