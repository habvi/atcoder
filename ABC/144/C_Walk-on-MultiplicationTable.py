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


n = int(input())

ans = float('inf')
for div in div_lis(n):
    ans = min(ans, (div - 1) + (n//div - 1))
print(ans)