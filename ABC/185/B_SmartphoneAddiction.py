n, m, t = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(m)]
bt = n
now = 0
for l, r in ab:
    bt -= l - now
    now = l
    if bt <= 0:
        print('No')
        exit()
    bt = min(n, bt + r - l)
    now += r - l
bt -= t - now
print('Yes' if bt > 0 else 'No')