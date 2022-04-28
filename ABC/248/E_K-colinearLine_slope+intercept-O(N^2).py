from collections import defaultdict
from fractions import Fraction

def slope_and_intercept(x1, y1, x2, y2):
    if x1 == x2:
        slp = 0
        itc = x1
    elif y1 == y2:
        slp = float('inf')
        itc = y1
    else:
        slp = Fraction(y2 - y1, x2 - x1)
        itc = y1 - slp * x1
    return slp, itc


n, K = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(n)]

if K == 1:
    print('Infinity')
    exit()

s = defaultdict(set)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        x, y = xy[i]
        x2, y2 = xy[j]
        slp, itc = slope_and_intercept(x, y, x2, y2)
        s[(slp, itc)].add(i)
        s[(slp,)].add(j)

for v in s.values():
    ans += (len(v) >= K)
print(ans)