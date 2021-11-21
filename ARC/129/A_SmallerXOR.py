n, l, r = map(int, input().split())
a = []
for i in range(len(bin(n)[2:])):
    if (n>>i) & 1 == 1:
        a.append((1<<i, (1<<(i+1)) - 1))

ans = 0
for x, y in a:
    if y < l: continue
    if r < x: break

    if x < l and r < y:
        ans += (r - l + 1)
    elif l <= x and y <= r:
        ans += (y - x + 1)
    elif x < l:
        ans += (y - max(x, l) + 1)
    else:
        ans += (min(y, r) - x + 1)
print(ans)