def accumulate_2d(A):
    for i in range(N + 1):
        for j in range(N):
            A[i][j + 1] += A[i][j]

    for i in range(N):
        for j in range(N + 1):
            A[i + 1][j] += A[i][j]


def get(A, ly, lx, ry, rx):
    return A[ry][rx] - A[ry][lx - 1] - A[ly - 1][rx] + A[ly - 1][lx - 1]


N = int(input())
A = []
for _ in range(N):
    B = [[0] * (N + 1)]
    for _ in range(N):
        B.append([0] + list(map(int, input().split())))
    A.append(B)

for a in A:
    accumulate_2d(a)

Q = int(input())
for _ in range(Q):
    x1, x2, y1, y2, z1, z2 = list(map(int, input().split()))
    ans = 0
    for i in range(x1 - 1, x2):
        ans += get(A[i], y1, z1, y2, z2)
    print(ans)
