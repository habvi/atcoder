n, k = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(n)]
x_st = sorted(xy, key=lambda x: x[0])
y_st = sorted(xy, key=lambda x: x[1])

ans = float('inf')
for i in range(n):
    for j in range(n):
        lx = x_st[i][0]
        ly = y_st[j][1]
        for ii in range(i+1, n):
            for jj in range(j+1, n):
                rx = x_st[ii][0]
                ry = y_st[jj][1]

                cnt = 0
                for x, y in xy:
                    if lx <= x <= rx and ly <= y <= ry:
                        cnt += 1
                if cnt >= k:
                    ans = min(ans, (rx - lx) * (ry - ly))
print(ans)