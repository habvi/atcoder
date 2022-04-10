n, X, Y = map(int, input().split())
A = list(map(int, input().split()))

B = []
new = []
for a in A:
    if Y <= a <= X:
        new.append(a)
    else:
        B.append(new)
        new = []
if new:
    B.append(new)

ans = 0
for C in B:
    mn, mx = -1, -1
    for i, c in enumerate(C):
        if c == X:
            mx = max(mx, i)
        if c == Y:
            mn = max(mn, i)

        if c == X:
            if mn != -1:
                ans += mn + 1
        elif c == Y:
            if mx != -1:
                ans += mx + 1
        else:
            if mn != -1 and mx != -1:
                ans += min(mn, mx) + 1
print(ans)