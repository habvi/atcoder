n = int(input())
mx = 100
xyh = []
for _ in range(n):
    x, y, h = map(int, input().split())
    if h != 0:
        x1, y1, h1 = x, y, h
    xyh.append((x, y, h))

for i in range(mx + 1):
    for j in range(mx + 1):
        H = h1 + abs(y1 - i) + abs(x1 - j)
        flg = True
        for x, y, h in xyh:
            if h == max(H - abs(y - i) - abs(x - j), 0):
                continue
            else:
                flg = False
                
        if flg:
            print(j, i, H)
            exit()