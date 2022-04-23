def calc(move, ms, rest, x):
    t = move + rest
    return (x // t * move + min(move, x % t)) * ms


a, b, c, d, e, f, X = map(int, input().split())

dist_t = calc(a, b, c, X)
dist_a = calc(d, e, f, X)

if dist_t == dist_a:
    print('Draw')
elif dist_t > dist_a:
    print('Takahashi')
else:
    print('Aoki')