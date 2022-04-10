from functools import lru_cache

@lru_cache(None)
def solve(x):
    if x == 1:
        return [1]

    return solve(x - 1) + [x] + solve(x - 1)


n = int(input())

print(*solve(n))