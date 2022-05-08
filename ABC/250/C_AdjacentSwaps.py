n, Q = map(int, input().split())

d = {i + 1 : i for i in range(n)}
A = list(range(1, n + 1))

for _ in range(Q):
    x = int(input())
    i = d[x]
    j = i + 1
    if j == n:
        j = i - 1

    nx = A[j]
    A[i], A[j] = A[j], A[i]
    d[x] = j
    d[nx] = i

print(*A)