n = int(input())
A = [0, *map(int, input().split()), 0]

dst = []
for i in range(n + 1):
    dst.append(abs(A[i] - A[i + 1]))

sm = sum(dst)
for i in range(1, n + 1):
    print(sm - dst[i - 1] - dst[i] + abs(A[i - 1] - A[i + 1]))