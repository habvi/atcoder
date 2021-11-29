n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1 = a[j][0] - a[i][0]
            y1 = a[j][1] - a[i][1]
            x2 = a[k][0] - a[j][0]
            y2 = a[k][1] - a[j][1]
            if x1 * y2 == y1 * x2:
                print('Yes')
                exit()
print('No')