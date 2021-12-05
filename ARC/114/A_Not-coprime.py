def pfact(x):
    res = []
    for i in range(2, int(x**0.5) + 1):
        while x % i == 0:
            x //= i
            res.append(i)
    if x >= 2: res.append(x)
    return res

from collections import defaultdict
from itertools import product
n = int(input())
x = list(map(int, input().split()))
d = defaultdict(list)
d2 = defaultdict(list)
for a in x:
    for p in set(pfact(a)):
        d[p].append(a)
        d2[a].append(p)

m = len(d)
ans = float('inf')
lis = list(d.keys())
for pr in product([0, 1], repeat=m):
    s = set()
    for i, p in enumerate(pr):
        if p:
            for el in d[lis[i]]:
                s.add(el)
    if len(s) == n:
        sk = 1
        for i, p in enumerate(pr):
            if p:
                sk *= lis[i]
        ans = min(ans, sk)
print(ans)