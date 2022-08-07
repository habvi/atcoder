n, Y = map(int, input().split())

for i in range(n + 1):
    for j in range(n + i - 1):
        k = (Y - 10000*i - 5000*j) // 1000
        if k < 0:
            continue
        if i + j + k == n:
            print(i, j, k)
            exit()
print(-1, -1, -1)


# ------------------------------
N, Y = map(int, input().split())

for x in range(N + 1):
    for y in range(N + 1):
        z = N - x - y
        if z < 0:
            continue
        if x * 10000 + y * 5000 + z * 1000 == Y:
            print(x, y, z)
            exit()
print(-1, -1, -1)