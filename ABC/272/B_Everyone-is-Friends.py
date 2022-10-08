N, M = map(int, input().split())

p = [[0] * N for _ in range(N)]
for _ in range(M):
    k, *x = map(int, input().split())
    for i in range(k):
        for j in range(i + 1, k):
            p[x[i] - 1][x[j] - 1] = 1

for i in range(N - 1):
    for j in range(i + 1, N):
        if not p[i][j]:
            print("No")
            exit()
print("Yes")