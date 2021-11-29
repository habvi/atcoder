def div_lis(x):
    div_l, div_r = [], []
    for i in range(1, int(x**0.5) + 1):
        if x % i != 0: continue
        div_l.append(i)
        if i != x // i:
            div_r.append(x // i)
    div = div_l + div_r[::-1]
    return div

n, m = map(int, input().split())
for d in reversed(div_lis(m)):
    if d * n <= m:
        print(d)
        exit()