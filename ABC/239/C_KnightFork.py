x1, y1, x2, y2 = map(int, input().split())

s = set()
for i in [-2, -1, 1, 2]:
    for j in [-2, -1, 1, 2]:
        if i == j or abs(i) == abs(j):
            continue
        s.add((x1 + i, y1 + j))

for i in [-2, -1, 1, 2]:
    for j in [-2, -1, 1, 2]:
        if i == j or abs(i) == abs(j):
            continue
        if (x2 + i, y2 + j) in s:
            print('Yes')
            exit()

print('No')