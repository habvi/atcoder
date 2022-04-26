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

def pfact(x):
    pfct = set()
    while x > 1:
        pfct.add(memo[x])
        x //= memo[x]
    return pfct


n, m = map(int, input().split())
A = list(map(int, input().split()))

mx = max(A)
memo = Sieve(mx)

ok = [1] * (m + 1)
ok[0] = 0
for a in set(A):
    for p in pfact(a):
        if p > m or not ok[p]:
            continue
        for x in range(p, m + 1, p):
            ok[x] = 0

print(sum(ok))
for i, x in enumerate(ok):
    if x:
        print(i)