n, m = map(int, input().split())

for c in range(n + 1):
    b = m - 2*n - 2*c
    a = n - b - c
    if a >= 0 and b >= 0 and c >= 0:
        print(a, b, c)
        exit()

print(-1, -1, -1)