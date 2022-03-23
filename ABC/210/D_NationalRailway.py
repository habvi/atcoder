def min_cost(A):
    global ans

    mn = [[INF] * w for _ in range(h)]
    mn[0][0] = A[0][0]

    for i in range(h):
        for j in range(w):
            if i == j == 0:
                continue

            if i - 1 >= 0:
                mn[i][j] = min(mn[i][j], mn[i - 1][j])
            if j - 1 >= 0:
                mn[i][j] = min(mn[i][j], mn[i][j - 1])

            cost = A[i][j] + C * (i + j)
            ans = min(ans, cost + mn[i][j])

            pre_cost = A[i][j] - C * (i + j)
            mn[i][j] = min(mn[i][j], pre_cost)


h, w, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

B = []
for a in A:
    B.append(tuple(reversed(a)))

INF = float('inf')
ans = INF
min_cost(A)
min_cost(B)

print(ans)