sx, sy, gx, gy = map(int, input().split())

dist = abs(sx - gx)
ys = sy + gy
if sx > gx:
    print(gx + dist * gy / ys)
else:
    print(sx + dist * sy / ys)