h, w = map(int, input().split())
R, C = map(lambda x: int(x) - 1, input().split())

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

ans = 0
for dy, dx in DXY:
    ny, nx = R + dy, C + dx
    if not (0 <= ny < h and 0 <= nx < w):
        continue
    ans += 1
print(ans)