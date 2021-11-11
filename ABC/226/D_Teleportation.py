from math import gcd
n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

s = set()
for i in range(n):
    for j in range(i+1, n):
        dx = xy[j][0] - xy[i][0]
        dy = xy[j][1] - xy[i][1]
        g = gcd(dx, dy)
        s.add((dx//g, dy//g))
        s.add((-dx//g, -dy//g))
print(len(s))