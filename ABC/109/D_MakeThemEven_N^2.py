h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
s
ans = []
for i in range(h - 1):
    for j in range(w):
        if a[i][j] % 2:
            a[i + 1][j] += 1
            ans.append((i + 1, j + 1, i + 2, j + 1))

for j in range(w - 1):
    if a[h - 1][j] % 2:
        a[h - 1][j + 1] += 1
        ans.append((h, j + 1, h, j + 2))

print(len(ans))
for a in ans:
    print(*a)