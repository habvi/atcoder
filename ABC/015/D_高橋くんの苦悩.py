W = int(input())
n, K = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(n)]

INF = float('inf')
dp = [[-INF] * (W + 1) for _ in range(K + 1)]
dp[0][0] = 0
for w, v in wv:
    for i in reversed(range(W + 1)):
        for m in range(K):
            if i + w <= W:
                dp[m + 1][i + w] = max(dp[m + 1][i + w], dp[m][i] + v)

ans = 0
for x in dp:
    ans = max(ans, max(x))
print(ans)