N = int(input())

d = [[None] * N for _ in range(N)]
x = 1
i, j = 0, 0
while x < N**2:
    while j + 1 < N and d[i][j + 1] is None:
        d[i][j] = x
        j += 1
        x += 1
    while i + 1 < N and d[i + 1][j] is None:
        d[i][j] = x
        i += 1
        x += 1
    while j - 1 >= 0 and d[i][j - 1] is None:
        d[i][j] = x
        j -= 1
        x += 1
    while i - 1 < N and d[i - 1][j] is None:
        d[i][j] = x
        i -= 1
        x += 1

middle = (N + 1) // 2
d[middle - 1][middle - 1] = "T"

for row in d:
    print(*row)
