from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 7)

@lru_cache(maxsize=None)
def solve(x):
    if x <= D:
        return 0

    (x1, y1), (x2, y2) = xy[x], xy[x - D]
    return solve(x - D) + abs(x1 - x2) + abs(y1 - y2)


h, w, D = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(h)]

xy = {}
for i in range(h):
    for j in range(w):
        xy[A[i][j]] = (i, j)

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(solve(r) - solve(l))