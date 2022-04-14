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