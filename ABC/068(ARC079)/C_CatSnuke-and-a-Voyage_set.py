n, m = map(int, input().split())

from_1 = set()
from_n = set()
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        from_1.add(b)
    if b == n:
        from_n.add(a)

print('POSSIBLE' if from_1 & from_n else 'IMPOSSIBLE')