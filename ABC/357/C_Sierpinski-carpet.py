def set_all_white(next, ni, nj, n):
    for i in range(n):
        for j in range(n):
            next[ni + i][nj + j] = "."


def copy_pre_to_next(pre, next, ni, nj, n):
    for i in range(n):
        for j in range(n):
            next[ni + i][nj + j] = pre[i][j]


def copy(pre, next, n):
    for i in range(0, n, n // 3):
        for j in range(0, n, n // 3):
            if i == j == n // 3:
                set_all_white(next, i, j, len(pre))
            else:
                copy_pre_to_next(pre, next, i, j, len(pre))


N = int(input())

pre = "#"
if N == 0:
    print(pre)
    exit(0)

for i in range(1, N + 1):
    next = [[""] * 3**i for _ in range(3**i)]
    copy(pre, next, 3**i)
    pre = next

for p in pre:
    print("".join(p))
