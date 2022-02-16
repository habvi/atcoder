x, y, a, b, c = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

mix = []
mix.extend((p, 0) for p in P)
mix.extend((q, 1) for q in Q)
mix.extend((r, 2) for r in R)
mix.sort(reverse=True)

total = x + y
ans = 0
for deli, k in mix:
    if total == 0:
        break

    if k == 0:
        if x:
            x -= 1
            total -= 1
            ans += deli
        else:
            continue
    elif k == 1:
        if y:
            y -= 1
            total -= 1
            ans += deli
        else:
            continue
    else:
        total -= 1
        ans += deli
print(ans)