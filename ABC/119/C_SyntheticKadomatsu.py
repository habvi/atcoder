from itertools import product
from collections import Counter

n, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(n)]

ans = float('inf')
for pr in product(range(4), repeat=n):
    c = Counter(pr)
    if not c[0] or not c[1] or not c[2]:
        continue

    bamboo = [[] for _ in range(3)]
    for i in range(n):
        if pr[i] == 3:
            continue
        bamboo[pr[i]].append(L[i])

    mp = 0
    for each, target in zip(bamboo, (A, B, C)):
        mp += (len(each) - 1) * 10
        mp += abs(sum(each) - target)
    ans = min(ans, mp)

print(ans)