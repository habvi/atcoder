from collections import defaultdict

n, W = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(n)]

dp = defaultdict(int)
dp[0] = 0

for w, v in wv:
    ndp = defaultdict(int)
    for nw, nv in dp.items():
        ndp[nw] = max(ndp[nw], nv)

        if w + nw > W:
            continue
        ndp[w + nw] = max(ndp[w + nw], v + nv)

    dp = ndp

print(max(dp.values()))