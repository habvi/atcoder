n, d, K = map(int, input().split())
lr = [tuple(map(int, input().split())) for _ in range(d)]
st = [tuple(map(int, input().split())) for _ in range(K)]
for i in range(K):
    s, t = st[i]
    if s < t:
        now = s
        for i, (l, r) in enumerate(lr, 1):
            if not (l <= now <= r):
                continue
            if l <= t <= r:
                print(i)
                break
            now = r
    else:
        now = s
        for i, (l, r) in enumerate(lr, 1):
            if not (l <= now <= r):
                continue
            if l <= t <= r:
                print(i)
                break
            now = l