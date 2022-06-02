from collections import defaultdict

D, n = map(int, input().split())
T = [int(input()) for _ in range(D)]

cloth = [[] for _ in range(D)]
for _ in range(n):
    a, b, c = map(int, input().split())
    for i, t in enumerate(T):
        if a <= t <= b:
            cloth[i].append(c)

INF = float('inf')
dp = defaultdict(lambda : -INF)
for c in cloth[0]:
    dp[c] = 0

for c in cloth[1:]:
    ndp = defaultdict(lambda : -INF)
    for now in c:
        for pre, pc in dp.items():
            ndp[now] = max(ndp[now], pc + abs(pre - now))
    dp = ndp

print(max(dp.values()))