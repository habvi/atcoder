from collections import Counter

def comb(n, r):
    n1, r = n + 1, min(r, n - r)
    nmrt = dnmnt = 1
    for i in range(1, r + 1):
        nmrt = nmrt * (n1 - i)
        dnmnt = dnmnt * i
    return nmrt // dnmnt


n = int(input())
A = list(map(int, input().split()))

c = Counter(A)
ans = comb(n, 3)
for v in c.values():
    if v >= 2:
        ans -= comb(v, 2) * (n - v)
    if v >= 3:
        ans -= comb(v, 3)
print(ans)