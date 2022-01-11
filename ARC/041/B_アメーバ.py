n, m = map(int, input().split())
b = [list(map(int, list(input()))) for _ in range(n)]
a = [["0"] * m for _ in range(n)]

for i in range(n - 2):
    for j in range(1, m - 1):
        if b[i][j]:
            k = b[i][j]
            b[i + 1][j - 1] -= k
            b[i + 1][j + 1] -= k
            b[i + 2][j] -= k
            a[i + 1][j] = str(k)
for ans in a:
    print("".join(ans))