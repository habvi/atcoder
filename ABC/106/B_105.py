def div_lis(x):
    div_l, div_r = [], []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i != 0:
            continue
        div_l.append(i)
        if i != x // i:
            div_r.append(x // i)
    div = div_l + div_r[::-1]
    return div


n = int(input())

ans = 0
for i in range(1, n + 1, 2):
    if len(div_lis(i)) == 8:
        ans += 1
print(ans)