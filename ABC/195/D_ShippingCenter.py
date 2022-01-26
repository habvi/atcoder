n, m, q = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(n)]
wv.sort(key=lambda x: (-x[1], x[0]))

X = list(map(int, input().split()))
for _ in range(q):
    l, r = map(int, input().split())
    A = X[:max(0, l - 1)] + X[r:]
    A.sort()
    
    used = set()
    ans = 0
    for a in A:
        for i, (w, v) in enumerate(wv):
            if i not in used:
                if w <= a:
                    ans += v
                    used.add(i)
                    break
    print(ans)