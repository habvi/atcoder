n, w = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0], reverse=True)

tg = 0
ans = 0
for y, g in ab:
    if tg + g <= w:
        tg += g
        ans += y * g
    else:
        ans += y * (w - tg)
        break
print(ans)