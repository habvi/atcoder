from functools import lru_cache

def ceil(x):
    return (x + 1) // 2

def floor(x):
    return x // 2


x = int(input())
MOD = 998244353

@lru_cache(maxsize=None)
def solve(x):
    if x <= 4:
        return x

    return solve(ceil(x)) * solve(floor(x)) % MOD

print(solve(x))