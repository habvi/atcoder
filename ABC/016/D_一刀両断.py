def cross_judge(x1, y1, x2, y2, x3, y3, x4, y4):
    tc1 = (x1 - x2)*(y3 - y1) + (y1 - y2)*(x1 - x3)
    tc2 = (x1 - x2)*(y4 - y1) + (y1 - y2)*(x1 - x4)
    td1 = (x3 - x4)*(y1 - y3) + (y3 - y4)*(x3 - x1)
    td2 = (x3 - x4)*(y2 - y3) + (y3 - y4)*(x3 - x2)
    return tc1*tc2 < 0 and td1*td2 < 0


ax, ay, bx, by = map(int, input().split())
n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
xy.append(xy[0])

cross = 0
for i in range(n):
    (x3, y3), (x4, y4) = xy[i], xy[i + 1]
    cross += cross_judge(ax, ay, bx, by, x3, y3, x4, y4)

print(cross // 2 + 1)