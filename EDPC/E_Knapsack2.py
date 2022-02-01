n, W = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(n)]

mx =  n * 1000 + 1
dp = [float('inf')] * mx
dp[0] = 0

for w, v in wv:
    for i in reversed(range(mx)):
        if i - v >= 0 and dp[i - v] != -1 and dp[i - v] + w <= W:
            dp[i] = min(dp[i], dp[i - v] + w)

for i, x in enumerate(reversed(dp)):
    if x <= W:
        print(mx - i - 1)
        exit()