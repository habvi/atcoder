from itertools import combinations
from collections import defaultdict

N = int(input())
KA = []
for _ in range(N):
    K, *A = map(int, input().split())
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    KA.append((K, d))

ans = 0
for (k1, A), (k2, B) in combinations(KA, 2):
    same = 0
    total = k1 * k2
    for a, num in A.items():
        if a in B:
            same += num * B[a]
    ans = max(ans, same / total)
print(ans)
