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


n, K = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
for mod in div_lis(total)[::-1]:
    B = [a % mod for a in A]
    B.sort()

    total = sum(B)
    plus = mod * n - sum(B)
    minus = 0
    for x in B:
        plus -= mod - x
        minus += x
        if minus <= K and plus <= K:
            print(mod)
            exit()