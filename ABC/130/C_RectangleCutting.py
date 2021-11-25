w, h, x, y = map(int, input().split())
cx, cy = w / 2, h / 2
s = w * h / 2
if cx == x and cy == y:
    print(s, 1)
else:
    print(s, 0)