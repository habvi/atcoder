h, w, C, q = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(q)]
a = a[::-1]

yk, tt = 0, 0
ans = [0] * C
seen_yk, seen_tt = set(), set()
for t, n, c in a:
    n, c = n-1, c-1
    if t == 1:
        if n in seen_yk: continue
        ans[c] += (w - tt)
        yk += 1
        seen_yk.add(n)
    else:
        if n in seen_tt: continue
        ans[c] += (h - yk)
        tt += 1
        seen_tt.add(n)
print(*ans)