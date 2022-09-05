from itertools import accumulate
import sys
sys.setrecursionlimit(10 ** 7)

def solve(L, R):
    if L + 1 == R:
        return 0
    if memo[L][R]:
        return memo[L][R]
    mn = float('inf')
    for mid in range(L + 1, R):
        cost = ac[R] - ac[L]
        mn = min(mn, solve(L, mid) + solve(mid, R) + cost)
    memo[L][R] = mn
    return mn


N = int(input())
A = [0, *map(int, input().split())]

ac = list(accumulate(A))
memo = [[0] * (N + 1) for _ in range(N + 1)]
print(solve(0, N))