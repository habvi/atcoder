from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

def ceil(x):
    return (x + 1) // 2

def floor(x):
    return x // 2


x = int(input())
MOD = 998244353

memo = defaultdict(int)

def f(x):
    if x <= 4:
        return x
    if x in memo:
        return memo[x]

    res = f(ceil(x)) * f(floor(x)) % MOD
    memo[x] = res
    return res

print(f(x) % MOD)