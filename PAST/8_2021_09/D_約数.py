def div_lis(x):
    div_l, div_r = [], []
    i = 1
    while i * i <= x:
        if x % i == 0:
            div_l.append(i)
            if i != x // i:
                div_r.append(x // i)
        i += 1
    div = div_l + div_r[::-1]
    return div


X, Y = map(int, input().split())

xd = len(div_lis(X))
yd = len(div_lis(Y))
if xd == yd:
    print('Z')
elif xd > yd:
    print('X')
else:
    print('Y')