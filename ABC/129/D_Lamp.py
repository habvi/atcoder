h, w = map(int, input().split())
s = [input() for _ in range(h)]
row = [[1] * w for _ in range(h)]
for i in range(h):
    for j in range(w - 1):
        if s[i][j] == "#":
            row[i][j] = -1
            continue
        if s[i][j + 1] == "#":
            row[i][j + 1] = -1
            continue
        row[i][j + 1] = row[i][j] + 1
for i in reversed(range(h)):
    for j in reversed(range(1, w)):
        if row[i][j] == -1 or row[i][j - 1] == -1:
            continue
        row[i][j - 1] = row[i][j]

col = [[1] * w for _ in range(h)]
for i in range(h - 1):
    for j in range(w):
        if s[i][j] == "#":
            col[i][j] = -1
            continue
        if s[i + 1][j] == "#":
            col[i + 1][j] = -1
            continue
        col[i + 1][j] = col[i][j] + 1
for i in reversed(range(1, h)):
    for j in reversed(range(w)):
        if col[i][j] == -1 or col[i - 1][j] == -1:
            continue
        col[i - 1][j] = col[i][j]

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            continue
        ans = max(ans, row[i][j] + col[i][j] - 1)
print(ans)