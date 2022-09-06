N, Q = map(int, input().split())

L = [None] * (N + 1)
R = [None] * (N + 1)
for _ in range(Q):
    t, *a = map(int, input().split())
    if t == 1:
        x, y = a
        R[x] = y
        L[y] = x
    elif t == 2:
        x, y = a
        R[x] = None
        L[y] = None
    else:
        x = a[0]
        l = []
        while L[x]:
            l.append(L[x])
            x = L[x]
        x = a[0]
        r = []
        while R[x]:
            r.append(R[x])
            x = R[x]

        ans = [*l[::-1], a[0], *r]
        print(len(ans), *ans)