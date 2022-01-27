n, q = map(int, input().split())

L = [-1] * (n + 1)
R = [-1] * (n + 1)
for _ in range(q):
    t, *a = map(int, input().split())
    if t == 1:
        x, y = a
        R[x] = y
        L[y] = x
    elif t == 2:
        x, y = a
        R[x] = -1
        L[y] = -1
    else:
        x = a[0]
        l, r = [], []
        nxt = x
        while L[nxt] != -1:
            l.append(L[nxt])
            nxt = L[nxt]

        nxt = x    
        while R[nxt] != -1:
            r.append(R[nxt])
            nxt = R[nxt]
        
        ans = [*l[::-1], x, *r]
        print(len(ans), *ans)