n, m, Q = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(n)]
X = list(map(int, input().split()))

wv.sort(key=lambda x: -x[1])

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    box = [*X[:l], *X[r:]]
    box.sort()

    ans = 0
    used = set()
    for b in box:
        for i, (w, v) in enumerate(wv):
            if i not in used and w <= b:
                ans += v
                used.add(i)
                break
    print(ans)