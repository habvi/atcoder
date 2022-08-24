from collections import defaultdict
from functools import lru_cache

@lru_cache(maxsize=None)
def red(r, x):
    if r == 1:
        return
    rnum[r] -= x
    rnum[r - 1] += x
    bnum[r] += X * x
    red(r - 1, rnum[r - 1])
    blue(r, bnum[r])

@lru_cache(maxsize=None)
def blue(b, x):
    if b == 1:
        return
    bnum[b] -= x
    rnum[b - 1] += x
    bnum[b - 1] += Y * x
    red(b - 1, rnum[b - 1])
    blue(b - 1, bnum[b - 1])


n, X, Y = map(int, input().split())

rnum = defaultdict(int)
bnum = defaultdict(int)
rnum[n] = 1

red(n, 1)
print(bnum[1])