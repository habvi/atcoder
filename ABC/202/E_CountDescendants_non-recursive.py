from bisect import bisect, bisect_left
from collections import defaultdict

def EulerTour(u):
    seen = [0] * n
    stack = [~u, u]
    d = -1
    num = 0
    while stack:
        v = stack.pop()
        if v < 0:
            out_[~v] = num
            dist[d].append(num)
            d -= 1
            num += 1
            continue

        seen[v] = 1
        d += 1
        dist[d].append(num)
        in_[v] = num
        num += 1

        for nv in g[v][::-1]:
            if seen[nv]:
                continue
            stack.append(~nv)
            stack.append(nv)


n = int(input())
P = list(map(lambda x: int(x) - 1, input().split()))

g = defaultdict(list)
for i, p in enumerate(P, 1):
    g[p].append(i)

dist = defaultdict(list)
in_ = [None] * n
out_ = [None] * n
EulerTour(0)

Q = int(input())
for _ in range(Q):
    u, d = map(int, input().split())
    u -= 1
    mn = in_[u]
    mx = out_[u]

    left = bisect_left(dist[d], mn)
    right = bisect(dist[d], mx)
    print((right - left) // 2)