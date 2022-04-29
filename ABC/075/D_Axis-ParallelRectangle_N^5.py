n, K = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(n)]

X = sorted(xy, key=lambda x: x[0])
Y = sorted(xy, key=lambda x: x[1])

ans = float('inf')
for i in range(n):
    for j in range(i + 1, n):
        lx, rx = X[i][0], X[j][0]

        for k in range(n):
            for l in range(k + 1, n):
                ly, ry = Y[k][1], Y[l][1]

                total = 0
                for x, y in xy:
                    if lx <= x <= rx and ly <= y <= ry:
                        total += 1

                if total >= K:
                    ans = min(ans, (rx - lx)*(ry - ly))
print(ans)