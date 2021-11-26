n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
for i in range(n):
    for j in range(n):
        if not (i+m <= n and j+m <= n): continue
        cnt = 0
        for k in range(m):
            for l in range(m):
                if a[i+k][j+l] == b[k][l]:
                    cnt += 1
        if cnt == m*m:
            print('Yes')
            exit()
print('No')