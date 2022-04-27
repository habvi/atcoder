from bisect import bisect_left

n, K, m, R = map(int, input().split())
S = [int(input()) for _ in range(n - 1)]

S.sort()
res = R * K
for _ in range(K - 1):
    res -= S.pop()

bi = bisect_left(S, res)
if bi == len(S):
    print(max(0, res) if res <= m else -1)
else:
    print(0)