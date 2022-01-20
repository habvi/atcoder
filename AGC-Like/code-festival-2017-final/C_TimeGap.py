from collections import Counter
from itertools import combinations

n = int(input())
D = list(map(int, input().split())) + [0]
c = Counter(D)

for v in c.values():
    if v >= 3:
        print(0)
        exit()
if c[0] >= 2 or c[12] >= 2:
    print(0)
    exit()

s = list(c.keys())
sn = len(s)

ans = 0
for bit in range(1 << sn):
    T = []
    for i in range(sn):
        k = s[i]
        if c[k] == 1:
            T.append((24 - k)%24 if bit>>i & 1 else k)
        elif c[k] == 2:
            T.append(k)
            T.append((24 - k)%24)
    
    mn = float('inf')
    for a, b in combinations(T, 2):
        d = abs(a - b)
        mn = min(mn, min(d, 24 - d))
    ans = max(ans, mn)
print(ans)