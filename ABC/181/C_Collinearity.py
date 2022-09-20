N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            if (x2 - x1) * (y3 - y2) == (y2 - y1) * (x3 - x2):
                print("Yes")
                exit()
print("No")