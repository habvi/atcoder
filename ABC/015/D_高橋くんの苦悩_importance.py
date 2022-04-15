W = int(input())
n, K = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(n)]

mx = 100 * n
INF = float('inf')
dp = [[INF] * (mx + 1) for _ in range(K + 1)]
dp[0][0] = 0
for w, v in wv:
    for pre in reversed(range(mx)):
        for m in range(K):
            if pre + v <= mx:
                dp[m + 1][pre + v] = min(dp[m + 1][pre + v], dp[m][pre] + w)

ans = 0
for i in range(K + 1):
    for j in reversed(range(mx + 1)):
        if dp[i][j] <= W:
            ans = max(ans, j)
            break
print(ans)