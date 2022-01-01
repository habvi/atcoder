h, w, x, y = map(int, input().split())
x, y = x - 1, y - 1
s = [input() for _ in range(h)]
ans = 1
for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
    ny, nx = x, y
    while True:
        ny, nx = ny + dy, nx + dx
        if not (0 <= ny < h and 0 <= nx < w):
            break
        if s[ny][nx] == "#":
            break
        ans += 1
print(ans)