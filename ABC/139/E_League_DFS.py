import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def get_id(a, b):
    if a > b:
        a, b = b, a
    return ids[(a, b)]

def dfs(v):
    if finished[v]:
        return dp[v]
    if seen[v] and not finished[v]:
        return -1
    seen[v] = 1
    dp[v] = 1
    for nv in g[v]:
        res = dfs(nv)
        if res == -1:
            return res
        dp[v] = max(dp[v], res + 1)
    finished[v] = 1
    return dp[v]


N = int(input())

g = defaultdict(set)
ids = defaultdict(lambda : -1)
num = 0
for i in range(N):
    B = list(map(lambda x: int(x) - 1, input().split()))
    for b in B:
        a = i
        if a > b:
            a, b = b, a
        if ids[(a, b)] == -1:
            ids[(a, b)] = num
            num += 1
    for j in range(N - 2):
        b, c = B[j], B[j + 1]
        l = get_id(i, b)
        r = get_id(i, c)
        g[r].add(l)

dp = [0] * num
seen = [0] * num
finished = [0] * num
ans = 0
for v in range(num):
    res = dfs(v)
    if res == -1:
        print(res)
        exit()
    ans = max(ans, res)
print(ans)