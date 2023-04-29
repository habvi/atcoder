def primes(max_number):
    pr = list(range(3, max_number + 1, 2))
    ln = len(pr)
    for i, k in enumerate(pr):
        if k:
            if k * k > max_number:
                break
            for j in range(i + k, ln, k):
                pr[j] = 0
    yield 2
    yield from [p for p in pr if p]

def is_ok(x):
    return a ** 2 * b * prime[x] ** 2 <= N

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


N = int(input())
limit = int(N ** 0.5) + 2
prime = list(primes(limit))
m = len(prime)
ans = 0
for i, a in enumerate(prime[:-2]):
    for j in range(i + 1, m - 1):
        b = prime[j]
        ci = bisect(m + 1, i + 1)
        if j + 1 <= ci:
            ans += ci - j
        else:
          break
print(ans)
