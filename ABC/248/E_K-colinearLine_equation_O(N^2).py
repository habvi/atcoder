from collections import defaultdict
from math import gcd

def equation_of_the_line(x1, y1, x2, y2):
    if x1 == x2:
        return 1, 0, -x1
    a = y2 - y1
    b = x1 - x2
    c = y1*x2 - x1*y2
    g = gcd(a, gcd(b, c))
    a, b, c = a // g, b // g, c // g
    if b < 0:
        return -a, -b, -c
    else:
        return a, b, c


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
        a, b, c = equation_of_the_line(x, y, x2, y2)
        s[(a, b, c)].add(i)
        s[(a, b, c)].add(j)

for v in s.values():
    ans += (len(v) >= K)
print(ans)