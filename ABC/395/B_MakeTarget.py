N = int(input())

g = [[''] * N for _ in range(N)]
for i in range(N):
    j = N - i
    if i > j:
        continue
    color = '.' if i % 2 else '#'
    for y in range(i, j):
        for x in range(i, j):
            g[y][x] = color

for row in g:
    print(''.join(row))
