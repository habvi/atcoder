def check(x, y):
    if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2:
        return True
    else:
        return False

cx, cy, r = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
if check(x1, y1) and check(x1, y2) and check(x2, y1) and check(x2, y2):
    print('YES')
    print('NO')
elif x1 <= cx - r and cx + r <= x2 and y1 <= cy - r and cy + r <= y2:
    print('NO')
    print('YES')
else:
    print('YES')
    print('YES')
    