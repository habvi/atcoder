from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 7)

@lru_cache(None)
def f(x, k):
    if k == 0:
        return 1

    if x < 10:
        if k == 1:
            return x
        else:
            return 0

    if len(str(x)) < k:
        return 0

    div, mod = divmod(x, 10)
    return f(div, k - 1) * mod + f(div, k) + f(div - 1, k - 1) * (9 - mod)


n = int(input())
K = int(input())

print(f(n, K))