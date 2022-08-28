H, W, D = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(H)]

xy = {}
for i in range(H):
    for j in range(W):
        xy[A[i][j]] = (i, j)

total = H * W
ac = [0] * (total + 1)
for num in range(1, D + 1):
    for i in range(num + D, total + 1, D):
        px, py = xy[i - D]
        x, y = xy[i]
        cost = abs(x - px) + abs(y - py)
        ac[i] = ac[i - D] + cost

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(ac[r] - ac[l])