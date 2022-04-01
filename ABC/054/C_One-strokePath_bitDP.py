from collections import defaultdict

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

dp = [[0] * n for _ in range(1 << n)]
dp[1][0] = 1
for now in range(1 << n):
    for v in range(n):
        if not now >> v & 1:
            continue

        for nv in g[v]:
            if now >> nv & 1:
                continue
            dp[now | 1 << nv][nv] += dp[now][v]

print(sum(dp[-1]))



# from collections import defaultdict

# n, m = map(int, input().split())
# g = defaultdict(int)
# for _ in range(m):
#     a, b = map(lambda x: int(x) - 1, input().split())
#     g[a] |= (1 << b)
#     g[b] |= (1 << a)

# dp = [[0] * n for _ in range(1 << n)]
# dp[1][0] = 1
# for now in range(1, 1 << n):
#     for v in range(n):
#         for nv in range(n):
#             if (v == nv) or (now >> nv & 1):
#                 continue
#             if not g[v] >> nv & 1:
#                 continue
#             dp[now | 1 << nv][nv] += dp[now][v]

# print(sum(dp[-1]))