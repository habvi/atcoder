def calc_dist(y1, y2) -> float:
    return (1 + (y2 - y1)**2) ** 0.5


n = int(input())
A = list(map(int, input().split()))

MX = 100
dist = [[0] * (MX + 1) for _ in range(MX + 1)]
for i in range(MX + 1):
    for j in range(MX + 1):
        dist[i][j] = calc_dist(i, j)

INF = float('inf')
# sum; pre
dp = [[INF] * (MX + 1) for _ in range(MX + 1)]
dp[0][0] = 0

for i in range(1, n):
    ndp = [[INF] * (MX + 1) for _ in range(MX + 1)]
    # pre : only 0
    if i == 1:
        for now in range(MX + 1):
            for p_total in range(MX + 1):
                if p_total + now <= MX:
                    ndp[now][p_total + now] = min(ndp[now][p_total + now]
                                                ,dp[0][p_total] + dist[now][0])
    # now : only 0
    elif i == n - 1:
        for pre in range(MX + 1):
            for p_total in range(MX + 1):
                ndp[0][p_total] = min(ndp[0][p_total]
                                    ,dp[pre][p_total] + dist[0][pre])
    else:
        for now in range(MX + 1):
            for pre in range(MX + 1):
                for p_total in range(MX + 1):
                    if p_total + now <= MX:
                        ndp[now][p_total + now] = min(ndp[now][p_total + now]
                                                    ,dp[pre][p_total] + dist[now][pre])
    dp = [l[:] for l in ndp]

total = sum(A)
print(dp[0][total])