def mh(A, B):
    x1, y1 = A
    x2, y2 = B
    return abs(x1 - x2) + abs(y1 - y2)


h, w, D = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(h)]

xy = {}
for i in range(h):
    for j in range(w):
        xy[A[i][j]] = (i, j)

hw = h * w
dist = [0] * (hw + 1)
for i in range(D + 1, hw + 1):
    if dist[i]:
        break
    for j in range(i, hw + 1, D):
        dist[j] = dist[j - D] + mh(xy[j], xy[j - D])

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(dist[r] - dist[l])